# Retail Sales Prediction

Este proyecto resuelve una prueba técnica de Analista de Datos con enfoque en IA. Consiste en construir un proceso ETL, almacenamiento en PostgreSQL/Supabase, predicción con un modelo de IA y visualización interactiva en Looker Studio.

## 🔧 Componentes

### 1. ETL
- Extracción de datos desde CSV simulado (Mockaroo) y API de clima (Open-Meteo).
- Limpieza y unión de datos.
- Predicción de ventas usando regresión lineal (`scikit-learn`).
- Carga a PostgreSQL.

### 2. Base de Datos
- Tabla `sales_predictions`.
- Consulta SQL para error promedio por categoría.
- Respaldo automático en Supabase.

### 3. Dashboard
- Looker Studio conectado a PostgreSQL.
- Visualizaciones: líneas, tabla de errores, mapa de calor.
- Filtros interactivos por fecha y categoría.

## 🚀 Cómo ejecutar

```bash
pip install -r requirements.txt
python etl/extract.py
python etl/transform.py
python etl/load.py
```

Configura la conexión a tu base de datos en un archivo `.env`.

## 📂 Estructura

```
retail-sales-prediction/
├── data/
├── etl/
├── model/
├── dashboard/
├── scripts/
└── README.md
```

## ✅ Requisitos

- Python 3.8+
- PostgreSQL
- Cuenta en Supabase (opcional para respaldo)

---

🧠 Prueba técnica para posición de Analista de Datos con IA.
