# ACHICRIP-ERP

Pequeño sistema de gestión de socios basado en FastAPI. Aún en etapas iniciales.

## Desarrollo

1. Crear entorno virtual e instalar dependencias:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload --app-dir backend
   ```

La API expone endpoints básicos para socios, pagos y eventos.
