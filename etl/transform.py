import pandas as pd
import logging
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from lightgbm import LGBMRegressor

# Configurar logging
log_path = "./logs"
os.makedirs(log_path, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{log_path}/transform.log"),
        logging.StreamHandler()
    ]
)

def remove_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Elimina outliers utilizando el método del rango intercuartílico (IQR).
    """
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df_clean = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df_clean

def transform():
    try:
        sales = pd.read_csv('etl/sales_raw.csv', parse_dates=['date'])
        weather = pd.read_csv('etl/weather_raw.csv', parse_dates=['date'])

        # Validar columnas
        expected_sales_cols = {"date", "product_id", "sales", "price", "category"}
        expected_weather_cols = {"date", "temperature"}
        if not expected_sales_cols.issubset(sales.columns) or not expected_weather_cols.issubset(weather.columns):
            raise ValueError("Columnas faltantes en los archivos de entrada")

        # Limpieza básica
        sales = sales.dropna()
        weather = weather.dropna()

        # Remover outliers en ventas y precios
        sales = remove_outliers(sales, "sales")
        sales = remove_outliers(sales, "price")

        # Merge
        df = pd.merge(sales, weather, on="date", how="left")
        df = df.dropna()

        X = df[["temperature", "price"]]
        y = df["sales"]

        # Modelo base: Regresión Lineal
        lr = LinearRegression()
        lr.fit(X, y)
        lr_preds = lr.predict(X)
        lr_mae = mean_absolute_error(y, lr_preds)
        df["lr_prediction"] = lr_preds

        # Modelo avanzado: LightGBM
        lgbm = LGBMRegressor(random_state=42)
        lgbm.fit(X, y)
        lgbm_preds = lgbm.predict(X)
        lgbm_mae = mean_absolute_error(y, lgbm_preds)
        df["lgbm_prediction"] = lgbm_preds

        # Elegir mejor modelo
        if lgbm_mae < lr_mae:
            df["sales_prediction"] = df["lgbm_prediction"]
            best_model = "LightGBM"
        else:
            df["sales_prediction"] = df["lr_prediction"]
            best_model = "Linear Regression"

        # Guardar salida
        df.to_csv("etl/sales_transformed.csv", index=False)

        logging.info(f"Transformación completada. Mejor modelo: {best_model}")
        logging.info(f"MAE LinearRegression: {lr_mae:.2f} | MAE LightGBM: {lgbm_mae:.2f}")
    except Exception as e:
        logging.error(f"Error en la transformación: {e}")
        raise

if __name__ == "__main__":
    transform()
