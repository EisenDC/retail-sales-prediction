import pandas as pd
from sklearn.linear_model import LinearRegression

def transform():
    # Cargar datos
    sales = pd.read_csv('etl/sales_raw.csv', parse_dates=['date'])
    weather = pd.read_csv('etl/weather_raw.csv', parse_dates=['date'])

    # Limpiar datos (ejemplo: eliminar filas con valores faltantes)
    sales = sales.dropna()
    weather = weather.dropna()

    # Unir datos por fecha (y producto si aplica)
    df = pd.merge(sales, weather[['date', 'temperature']], on='date', how='left')

    # Preparar variables para el modelo
    # Usaremos temperatura y precio para predecir ventas
    X = df[['temperature', 'price']]
    y = df['sales']

    # Entrenar modelo de regresión lineal
    model = LinearRegression()
    model.fit(X, y)

    # Predecir ventas
    df['sales_prediction'] = model.predict(X)

    # Guardar resultado en CSV (o JSON)
    df.to_csv('etl/sales_transformed.csv', index=False)
    print("Transformación completada. Archivo guardado: etl/sales_transformed.csv")

if __name__ == "__main__":
    transform()
