from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import numpy as np
import shutil
import os
import lightkurve as lk
from exoplanet_ml import predict_exoplanet_status

app = FastAPI()

app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../templates")

UPLOAD_DIR = "../uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request, fits_file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, fits_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(fits_file.file, buffer)

    try:
        pixel_file = lk.open(file_path)
        lc = pixel_file.to_lightcurve(aperture_mask=pixel_file.pipeline_mask)
        flat_lc = lc.flatten()

        # Extract time and flux for Chart.js
        time_values = flat_lc.time.value.tolist()
        flux_values = flat_lc.flux.value.tolist()

        # Run BLS
        period = np.linspace(1, 5, 10000)
        bls = lc.to_periodogram(method="bls", period=period, frequency_factor=500)

        planet_x_period = bls.period_at_max_power.value
        planet_x_t0 = bls.transit_time_at_max_power.value
        planet_x_dur = bls.duration_at_max_power.value
        exoplanet_radius = np.sqrt((planet_x_dur * planet_x_period) / np.pi)

        features = pd.DataFrame(
            {
                "Orbital period": [planet_x_period],
                "transit duration": [planet_x_dur],
                "radii(planet)": [exoplanet_radius],
            }
        )

        exo_status = predict_exoplanet_status(features)
        result = (
            f"It is a {exo_status.lower()} exoplanet."
            if exo_status[0] in ["CONFIRMED", "CANDIDATE"]
            else "It is not an exoplanet."
        )

        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "result": result,
                "period": planet_x_period,
                "t0": planet_x_t0,
                "duration": planet_x_dur,
                "radius": exoplanet_radius,
                "time": time_values,
                "flux": flux_values,
            },
        )
    except Exception as e:
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "result": f"Error processing file: {e}",
                "period": "-",
                "t0": "-",
                "duration": "-",
                "radius": "-",
                "time": [],
                "flux": [],
            },
        )


if __name__ == "__main__":
    from uvicorn import run

    run(app)
