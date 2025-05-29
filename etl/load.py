import pandas as pd
import logging
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Configurar logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Cargar variables de entorno desde .env
load_dotenv()

# Leer variables del entorno
usuario = os.getenv("DB_USER")
contrasena = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = os.getenv("DB_PORT")
base_datos = os.getenv("DB_NAME")

# Validar que todas las variables estén presentes
if not all([usuario, contrasena, host, puerto, base_datos]):
    logging.error("❌ Faltan variables de conexión en el archivo .env.")
    exit(1)

# Crear la conexión
try:
    engine = create_engine(f"postgresql://{usuario}:{contrasena}@{host}:{puerto}/{base_datos}")
    logging.info("🔗 Conexión a la base de datos establecida.")
except Exception as e:
    logging.error(f"❌ Error al conectar a la base de datos: {e}")
    exit(1)

# Cargar DataFrame transformado
try:
    df = pd.read_csv("etl/sales_transformed.csv")
    df.to_sql("sales_predictions", con=engine, if_exists="append", index=False)
    logging.info("✅ Datos cargados exitosamente en la tabla sales_predictions.")
except Exception as e:
    logging.error(f"❌ Error al cargar datos a PostgreSQL: {e}")
    exit(1)
