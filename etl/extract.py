import pandas as pd
import requests
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_sales_data(csv_path: str) -> pd.DataFrame:
    logging.info(f"Cargando datos de ventas desde {csv_path}")
    sales_df = pd.read_csv(csv_path, parse_dates=["date"])
    logging.info(f"Datos de ventas cargados: {len(sales_df)} filas")
    return sales_df

def fetch_weather_data(start_date: str, end_date: str, latitude: float, longitude: float) -> pd.DataFrame:
    logging.info(f"Consultando API de clima desde {start_date} hasta {end_date}")
    # Ejemplo con Open-Meteo: clima diario temperatura media
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={latitude}&longitude={longitude}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min&timezone=America/Bogota"
    )
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    # Transformar datos en DataFrame
    df = pd.DataFrame({
        "date": pd.to_datetime(data["daily"]["time"]),
        "temp_max": data["daily"]["temperature_2m_max"],
        "temp_min": data["daily"]["temperature_2m_min"]
    })
    # Calcular temperatura promedio
    df["temperature"] = (df["temp_max"] + df["temp_min"]) / 2
    df = df.drop(columns=["temp_max", "temp_min"])
    
    logging.info(f"Datos de clima obtenidos: {len(df)} filas")
    return df

if __name__ == "__main__":
    sales_csv = "./data/sales_data.csv"  # Ajusta la ruta según tu proyecto
    sales_df = load_sales_data(sales_csv)
    
    start_date = sales_df["date"].min().strftime("%Y-%m-%d")
    end_date = sales_df["date"].max().strftime("%Y-%m-%d")
    
    # Coordenadas ejemplo (Bogotá)
    latitude = 4.7110
    longitude = -74.0721
    
    weather_df = fetch_weather_data(start_date, end_date, latitude, longitude)
    
    # Guardar data extraída
    sales_df.to_csv("./etl/sales_raw.csv", index=False)
    weather_df.to_csv("./etl/weather_raw.csv", index=False)
    
    logging.info("Extracción finalizada y datos guardados en ./etl/")
