🛍️ Retail Sales Prediction


Este proyecto fue desarrollado como parte de una prueba técnica para una posición de Analista de Datos con enfoque en Inteligencia Artificial. 
El objetivo es construir un pipeline de análisis completo: desde la recopilación de datos hasta la visualización interactiva de resultados.


🔧 Componentes del Proyecto

1. ETL (Extract – Transform – Load)

Extracción de datos desde un archivo CSV simulado (Mockaroo) y la API de clima Open-Meteo.


Transformación: limpieza, unión de fuentes, ingeniería de variables y predicción de ventas con un modelo de regresión lineal utilizando scikit-learn.


Carga de los datos transformados a una base de datos PostgreSQL local o en la nube (Supabase).



2. Base de Datos (PostgreSQL/Supabase)

Tabla principal: sales_predictions.

Campos clave: date, category, sales, sales_prediction, temperature, error_absoluto.

Incluye una consulta SQL para obtener el error promedio por categoría.

Opción de respaldo automático a Supabase.



3. 📊 Visualización en Looker Studio

https://lookerstudio.google.com/reporting/ad0e008d-7869-40aa-b52e-3f7ca6962567


Tablero conectado directamente a PostgreSQL.


Elementos visuales:


📈 Gráfico de líneas: ventas reales vs. predicciones por fecha.


📋 Tabla de errores: promedio de error absoluto por categoría.


🌡️ Mapa de calor: ventas por categoría y temperatura, con formato condicional.


🔍 Filtros interactivos: por fecha y categoría.


🚀 Cómo ejecutar el proyecto

Clona el repositorio:


bash

git clone https://github.com/EisenDC/retail-sales-prediction.git
cd retail-sales-prediction

Instala las dependencias:


pip install -r requirements.txt
Configura tu entorno:


Crea un archivo .env en la raíz del proyecto con la siguiente configuración:

env

DB_USER=tu_usuario

DB_PASSWORD=tu_contraseña

DB_HOST=localhost

DB_PORT=5432

DB_NAME=nombre_de_tu_base_de_datos

Ejecuta el pipeline ETL:

bash

python etl/extract.py

python etl/transform.py

python etl/load.py



📁 Estructura del Proyecto


retail-sales-prediction/

├── data/                  # Datos de entrada (CSV y backups)

├── etl/                   # Scripts ETL: extract.py, transform.py, load.py

├── model/                 # Entrenamiento del modelo de IA

├── dashboard/             # Capturas o enlaces al dashboard

├── scripts/               # SQLs y scripts adicionales

├── requirements.txt       # Dependencias del proyecto

└── README.md              # Documentación del proyecto
