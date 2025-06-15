# ACHICRIP-ERP

Pequeño sistema de gestión de socios basado en FastAPI y React. Aún en etapas iniciales.

## Desarrollo

1. Crear entorno virtual e instalar dependencias:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. Ejecutar el servidor backend:
   ```bash
   uvicorn app.main:app --reload --app-dir backend
   ```

### Frontend

1. Instalar dependencias de Node (solo la primera vez):
   ```bash
   cd frontend
   npm install
   ```
2. Levantar el servidor de desarrollo:
   ```bash
   npm run dev
   ```
   Esto abre la aplicación en `http://localhost:5173`.

La API expone endpoints básicos para socios, pagos y eventos y el frontend permite probarlos vía navegador.
