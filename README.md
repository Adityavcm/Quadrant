# 🔭 The Quadrant - Exoplanet Analyzer

Welcome to **The Quadrant**, a modern web-based platform to analyze exoplanet transit data using machine learning

---

## 🚀 Features

- 🌌 Upload `.fits` light curve files
- 📈 Visualize time vs flux using Chart.js
- 🤖 Predict exoplanet status
- 💻 FastAPI backend with HTML/CSS/JavaScript frontend

---

## 🗂 Project Structure

```

.
├── backend/
│ ├── main.py # FastAPI app
│ ├── exoplanet_ml.py # ML model loading & prediction
│ ├── utils.py # Light curve extraction utilities
│ └── uploads/ # Uploaded .fits files
├── data/
│ ├── exoplanet.csv # Training dataset for ML
│ └── sample.fits # Sample light curve
├── static/
│ └── style.css # CSS styles
├── templates/
│ ├── index.html # Homepage
│ └── results.html # Output + graph
├── legacy/ # Original tkinter version
├── requirements.txt
├── dir.py # Directory viewer utility
└── README.md # You're here!

```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/SrinidhiPRao/Quadrant.git
cd Quadrant
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🏃 Run the App

```bash
uvicorn backend.main:app --reload
```

Then open your browser and visit:
➡️ `http://127.0.0.1:8000/`

---

## 📚 Tech Stack

- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **ML:** Random Forest (scikit-learn)
- **Astro Processing:** lightkurve
- **Charting:** Chart.js

---

## 📬 Contact

Made with ❤️ by [Aditya Chapparadhallimath](https://github.com/Adityavcm), [S K Avinash](https://github.com/Aviator1223), [Rohith Kuruvilla](https://github.com/Rohith-X-Kuruviulla-P) and [Srinidhi P Rao](https://github.com/SrinidhiPRao)

> Feel free to reach out for suggestions, collaborations, or issues!

---

## 📝 License

MIT License. See `LICENSE` file for details.
