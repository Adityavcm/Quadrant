import lightkurve as lk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from exoplanet_ml import predict_exoplanet_status
import os


def process_fits(file_path: str):
    pixelFile = lk.open(file_path)
    lc = pixelFile.to_lightcurve(aperture_mask=pixelFile.pipeline_mask)
    flat_lc = lc.flatten()

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

    status = predict_exoplanet_status(features)[0]

    return {
        "Orbital period": planet_x_period,
        "Transit time": planet_x_t0,
        "Transit duration": planet_x_dur,
        "Radius": exoplanet_radius,
        "Status": status,
    }
