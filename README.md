# ACHICRIP-ERP


## Paso a paso para comenzar

### 1. Clonar el repositorio

Necesitas tener `git` instalado. Desde una terminal ejecuta:

```bash
git clone https://github.com/<tu-usuario>/ACHICRIP-ERP.git
cd ACHICRIP-ERP
```

### 2. Preparar el entorno de Python

Asegúrate de contar con Python 3.10 o superior. Crea un entorno virtual e instala las dependencias del backend:

```bash
python3 -m venv .venv        # crea el entorno
source .venv/bin/activate    # actívalo (en Windows usa .venv\Scripts\activate)
pip install -r backend/requirements.txt
```

### 3. Instalar dependencias del frontend

También se requiere Node.js con npm. Ejecuta una vez:

```bash
cd frontend
npm install
cd ..
```

### 4. Ejecutar el backend

Con el entorno virtual activo, lanza FastAPI en un terminal:

```bash
uvicorn app.main:app --reload --app-dir backend --port 8000
```

### 5. Ejecutar el frontend

En otra terminal, dentro de la carpeta `frontend`:

```bash
cd frontend
npm run dev
```

Visita `http://localhost:5173` en tu navegador para probar la aplicación. La API estará en `http://localhost:8000`.

### 6. Detener servidores y salir

Presiona `Ctrl+C` para detener cada servidor. Para cerrar el entorno virtual ejecuta `deactivate`.

---
   ```bash
   npm run dev
   ```
   Esto abre la aplicación en `http://localhost:5173`.

La API expone endpoints básicos para socios, pagos y eventos y el frontend permite probarlos vía navegador.

