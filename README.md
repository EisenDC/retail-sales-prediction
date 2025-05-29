🛍️ Retail Sales Prediction
Este proyecto fue desarrollado como parte de una prueba técnica para una posición de Analista de Datos con enfoque en Inteligencia Artificial. El objetivo es construir un pipeline de análisis completo: desde la recopilación de datos hasta la visualización interactiva de resultados.

🔧 Componentes del Proyecto
1. ETL (Extract – Transform – Load)
Extracción de datos desde un archivo CSV simulado (Mockaroo) y API de clima Open-Meteo.

Transformación: limpieza, unión de fuentes, ingeniería de variables y predicción de ventas con modelo de regresión lineal (scikit-learn).

Carga a una base de datos PostgreSQL local o en la nube (Supabase).

2. Base de Datos (PostgreSQL/Supabase)
Tabla principal: sales_predictions.

Campos clave: date, category, sales, sales_prediction, temperature, error_absoluto.

Incluye una consulta SQL para obtener el error promedio por categoría.

Opción de respaldo automático a Supabase.

3. Visualización Interactiva (Looker Studio)
Tablero conectado directamente a PostgreSQL.

Elementos visuales:

📈 Gráfico de líneas: ventas reales vs. predicciones por fecha.

📋 Tabla de errores: promedio de error absoluto por categoría.

🌡️ Mapa de calor: ventas por categoría y temperatura, con formato condicional.

🔍 Filtros interactivos: por fecha y categoría.

🚀 Cómo ejecutar el proyecto
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/tu_usuario/retail-sales-prediction.git
cd retail-sales-prediction
Instala dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Configura tu entorno:
Crea un archivo .env con la configuración de tu base de datos:

ini
Copiar
Editar
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nombre_basededatos
Ejecuta el pipeline ETL:

bash
Copiar
Editar
python etl/extract.py
python etl/transform.py
python etl/load.py
📊 Visualización en Looker Studio
El dashboard se encuentra en el archivo dashboard/looker_studio_report.png.

O visita el reporte en línea (si está disponible públicamente).

Incluye:

Gráfico comparativo de ventas vs. predicción.

Tabla con error promedio por categoría.

Mapa de calor por temperatura y categoría.

Filtros para navegación por fecha y tipo de producto.

📁 Estructura del Proyecto
bash
Copiar
Editar
retail-sales-prediction/
├── data/                  # Datos de entrada (CSV y backups)
├── etl/                   # Scripts ETL: extract.py, transform.py, load.py
├── model/                 # Entrenamiento del modelo de IA
├── dashboard/             # Capturas o enlaces al dashboard
├── scripts/               # SQLs y scripts adicionales
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación del proyecto



