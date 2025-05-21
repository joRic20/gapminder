# Gapminder Bubble Chart Dashboard

A Streamlit-based interactive dashboard visualizing global Life Expectancy, Population, and GNI per Capita (PPP) over time, using Gapminder data. Provides an animated bubble chart with a year slider and multi-country selection.

---

## 📁 Project Structure

```
├── data/
│   ├── population.csv             # Raw population data
│   ├── life_expectancy.csv        # Raw life expectancy data
│   ├── gni_per_capita.csv         # Raw GNI per capita (PPP) data
│   └── processed/
│       └── merged_gapminder.csv   # Merged & cleaned dataset
│
├── notebooks/
│   └── 01_data_preparation.ipynb  # Jupyter notebook for data loading & preprocessing
│
├── src/
│   ├── requirements.txt           # Python dependencies
│   └── app.py                     # Streamlit dashboard application
│
├── Dockerfile                     # Container specification for production
├── docker-compose.dev.yml         # (Optional) Compose file for local development
├── captain-definition             # CapRover build instructions
└── README.md                      # This file
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* Docker
* (Optional) Docker Compose
* CapRover CLI (`npm install -g caprover`) if deploying via CapRover

### 1. Data Preparation

Data is preprocessed in the Jupyter notebook. To generate the merged CSV:

```bash
# From project root
jupyter nbconvert --to notebook --execute notebooks/01_data_preparation.ipynb
```

This creates `data/processed/merged_gapminder.csv` by:

1. Loading the three raw CSVs.
2. Forward-filling missing values per country.
3. Melting each into a tidy format.
4. Merging on country & year into a 5-column table.

### 2. Local Development (Docker)

Build an image and run without auto-reload:

```bash
# Build the image
docker build -t gapminder .

# Run the container (mount data for live updates)
docker run -it --rm \
  -p 8501:8501 \
  -v "$(pwd)/src":/app/src \
  -v "$(pwd)/data/processed":/app/data/processed \
  gapminder
```

Open your browser at [http://localhost:8501](http://localhost:8501).

### 3. Production Deployment with CapRover

1. Ensure `captain-definition` is present at root:

   ```json
   {
     "schemaVersion": 2,
     "dockerfilePath": "./Dockerfile"
   }
   ```
2. Commit & push to GitHub.
3. Run:

   ```bash
   caprover deploy --default --appName ahh
   ```
4. Visit my live dashboard at [https://gapminder.quandev.xyz](https://gapminder.quandev.xyz).

---

## 🛠️ Development Commands

* **Rebuild image**: `docker build -t gapminder .`
* **Run dev container**: see section 2 above
* **Stop & clean containers**: `docker rm -f $(docker ps -a -q --filter ancestor=gapminder)`

---

## 📝 License & Author

© 2025 Richard Quansah

---

Enjoy exploring global trends with your Bubble Chart Dashboard! Feel free to open issues or pull requests. global trends with your Bubble Chart Dashboard! Feel free to open issues or pull requests.

