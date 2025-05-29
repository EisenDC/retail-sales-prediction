import pandas as pd
import requests
import logging
from datetime import datetime
import os

# Configurar logging
log_path = "./logs"
os.makedirs(log_path, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{log_path}/extract.log"),
        logging.StreamHandler()
    ]
)

def load_sales_data(csv_path: str) -> pd.DataFrame:
    """
    Carga datos de ventas desde un archivo CSV.
    """
    try:
        sales_df = pd.read_csv(csv_path, parse_dates=["date"])
        if not {"date", "product_id", "sales", "price", "category"}.issubset(sales_df.columns):
            raise ValueError("El CSV de ventas no contiene todas las columnas necesarias.")
        logging.info(f"Datos de ventas cargados correctamente: {len(sales_df)} filas.")
        return sales_df
    except Exception as e:
        logging.error(f"Error al cargar datos de ventas: {e}")
        raise

def fetch_weather_data(start_date: str, end_date: str, latitude: float, longitude: float) -> pd.DataFrame:
    """
    Consulta datos de clima desde la API Open-Meteo.
    """
    try:
        url = (
            f"https://archive-api.open-meteo.com/v1/archive?"
            f"latitude={latitude}&longitude={longitude}"
            f"&start_date={start_date}&end_date={end_date}"
            f"&daily=temperature_2m_max,temperature_2m_min&timezone=America/Bogota"
        )
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        df = pd.DataFrame({
            "date": pd.to_datetime(data["daily"]["time"]),
            "temperature": (pd.Series(data["daily"]["temperature_2m_max"]) +
                            pd.Series(data["daily"]["temperature_2m_min"])) / 2
        })

        logging.info(f"Datos de clima obtenidos correctamente: {len(df)} filas.")
        return df
    except Exception as e:
        logging.error(f"Error al consultar API de clima: {e}")
        raise

if __name__ == "__main__":
    try:
        os.makedirs("./etl", exist_ok=True)
        sales_csv = "./data/sales_data.csv"
        sales_df = load_sales_data(sales_csv)
        
        start_date = sales_df["date"].min().strftime("%Y-%m-%d")
        end_date = sales_df["date"].max().strftime("%Y-%m-%d")
        
        # Coordenadas de Bogotá
        latitude = 4.7110
        longitude = -74.0721
        
        weather_df = fetch_weather_data(start_date, end_date, latitude, longitude)

        # Guardar archivos de salida
        sales_df.to_csv("./etl/sales_raw.csv", index=False)
        weather_df.to_csv("./etl/weather_raw.csv", index=False)
        logging.info("Extracción finalizada y datos guardados en './etl/'.")
    except Exception as e:
        logging.critical(f"Falló el proceso de extracción: {e}")
