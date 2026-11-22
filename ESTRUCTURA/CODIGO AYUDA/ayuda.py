"""
# Ir a la carpeta AEROLISTA
cd "C:\PROYECTO_ESTRUCTURA\TERCER-SEMESTRE\ESTRUCTURA\GUIAS PRACTICAS\GUIA_4_AEROLISTA\AEROLISTA"

# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
.\venv\Scripts\Activate.ps1

# Instalar las dependencias
python -m pip install -r requirements.txt

# Ver la carpeta actual y sus archivos
pwd
dir

# Ejecutar la aplicación
python app.py

# Guardar la lista actual de dependencias
python -m pip freeze > requirements.txt

# Salir del entorno virtual
deactivate
"""