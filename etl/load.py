import pandas as pd
from sqlalchemy import create_engine

# Cargar el DataFrame transformado
df = pd.read_csv("etl/sales_transformed.csv")

# Reemplaza con tus credenciales reales
usuario = "miusuario"
contrasena = "Clave"
host = "localhost"
puerto = "5432"
base_datos = "salesdb"

# Crear engine de conexión
engine = create_engine(f"postgresql://{usuario}:{contrasena}@{host}:{puerto}/{base_datos}")

# Cargar datos a la tabla sales_predictions
df.to_sql("sales_predictions", con=engine, if_exists="append", index=False)

print("✅ Datos cargados exitosamente a PostgreSQL.")
