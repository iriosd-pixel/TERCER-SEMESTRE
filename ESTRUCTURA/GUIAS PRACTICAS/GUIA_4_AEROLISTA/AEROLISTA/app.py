# ==============================================================
#  app.py  ·  El servidor de AeroLista
#  Desde ahora, cada paso agrega sus rutas nuevas ENCIMA de la
#  línea que dice ENCENDER EL SERVIDOR (casi al final del archivo).
# ==============================================================

import traceback                       # 🆕 (paso 28) muestra errores completos en la terminal

# Flask:           crea la aplicación
# jsonify:         🆕 convierte un dict de Python en una respuesta JSON
# render_template: busca un archivo dentro de templates/ y lo entrega
# request:         🆕 (paso 29) permite leer lo que nos manda el navegador
from flask import Flask, jsonify, render_template, request
from werkzeug.exceptions import HTTPException   # 🆕 (paso 28) errores web como "404 no existe"


# 🆕 Traemos el diccionario VUELO que está en vuelo.py
from vuelo import VUELO

app = Flask(__name__)


@app.get("/")
def inicio():
    # 🆕 render_template hace 3 cosas:
    #    1. busca templates/index.html
    #    2. reemplaza cada {{ vuelo.algo }} con el dato de este diccionario
    #       (por ejemplo {{ vuelo.origen }} → "Guayaquil")
    #    3. envía el HTML ya completo al navegador
    return render_template("index.html", vuelo=VUELO)

# ==============================================================
#  RESPUESTAS DE LA API: todas tienen la misma forma
#     { "ok": true/false, "datos": ..., "mensaje": "...", "avisos": [...] }
# ==============================================================
def respuesta_ok(datos=None, mensaje="", avisos=None, codigo=200):
    """Respuesta de ÉXITO. codigo 200 = 'todo bien' (201 = 'creado')."""
    return jsonify({
        "ok": True,                 # salió bien
        "datos": datos,             # lo que pidió el navegador
        "mensaje": mensaje,         # un texto para mostrar al usuario
        "avisos": avisos or [],     # advertencias opcionales (si no hay, lista vacía)
    }), codigo


def respuesta_error(mensaje, codigo=400):
    """Respuesta de ERROR. 400 = datos incorrectos · 404 = no existe."""
    return jsonify({"ok": False, "mensaje": mensaje}), codigo


# ==============================================================
#  API: rutas que responden JSON (las llama el JavaScript)
# ==============================================================
@app.get("/api/vuelo")
def ver_vuelo():
    """Datos del avión: el JavaScript los usa para DIBUJAR filas y asientos."""
    return respuesta_ok(VUELO)      # el diccionario VUELO viaja como JSON


# ===== ENCENDER EL SERVIDOR =====
if __name__ == "__main__":
    app.run(debug=True, port=5050)
