"""
# =========================
# AEROLISTA
# =========================
cd "C:\PROYECTO_ESTRUCTURA\TERCER-SEMESTRE\ESTRUCTURA\GUIAS PRACTICAS\GUIA_4_AEROLISTA\AEROLISTA"

# Crear y activar el entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instalar dependencias y comprobar la carpeta
python -m pip install -r requirements.txt
pwd
dir

# Ejecutar AeroLista
python app.py

# Para detener Flask, pulsa Ctrl+C.
# Después puedes salir del entorno virtual:
deactivate

# Opcional: actualiza requirements.txt con las dependencias instaladas.
# Este comando sobrescribe el archivo.
python -m pip freeze > requirements.txt


# =========================
# GUÍA DE PILAS Y COLAS
# =========================
cd "C:\PROYECTO_ESTRUCTURA\TERCER-SEMESTRE\ESTRUCTURA\GUIAS PRACTICAS\GUIA_3_PILAS_COLAS"
pwd
dir
python .\main.py


# =========================
# GUÍAS DE LISTAS
# =========================
cd "C:\PROYECTO_ESTRUCTURA\TERCER-SEMESTRE\ESTRUCTURA\GUIAS GENERAL"
pwd
dir

# Ejecuta una línea por vez:
python ".\Listas.py"
python ".\listas enlazadas.py"


# =========================
# TAREA DE LISTAS
# =========================
cd "C:\PROYECTO_ESTRUCTURA\TERCER-SEMESTRE\ESTRUCTURA\TAREAS\Tarea listas"
pwd
dir
python .\main.py
"""




"""# Primera ejecución en una computadora nueva

# Entra a la carpeta AEROLISTA.
# Cambia esta ruta si descomprimiste la carpeta en otro lugar.
cd "$HOME\Downloads\GUIA_4_AEROLISTA\AEROLISTA"

# Crea el entorno virtual y actívalo.
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instala las dependencias del proyecto.
python -m pip install -r requirements.txt

# Ejecuta la aplicación.
python app.py"""



"""Cuando abras otra terminal para volver a ejecutar AeroLista:
cd "$HOME\Downloads\GUIA_4_AEROLISTA\AEROLISTA"
.\venv\Scripts\Activate.ps1
python app.py

Keyword arguments:
argument -- description
Return: return_description
"""
#deactivate