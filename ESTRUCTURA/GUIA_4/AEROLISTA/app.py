# ==============================================================
#  app.py  ·  El servidor de AeroLista
#  Versión 1: solo saluda, para comprobar que Flask funciona.
# ==============================================================

# 1) Importamos (traemos) la clase Flask desde la librería flask
#    que instalamos con "pip install flask".
from flask import Flask, render_template
from vuelo import VUELO
# 2) Creamos la aplicación y la guardamos en la variable "app".
#    __name__ le dice a Flask dónde está este archivo; así después
#    sabrá encontrar las carpetas templates/ y static/.
app = Flask(__name__)


# 3) Una RUTA. Se lee: "cuando el navegador pida la dirección / (la
#    página principal) con el método GET, ejecuta la función de abajo".
#    El símbolo @ indica un DECORADOR: "adorna" la función inicio()
#    conectándola con esa dirección.
@app.get("/reserva")
def inicio():
    # Lo que la función RETORNA es lo que el navegador mostrará.
    # Por ahora es un texto con un poco de HTML (<h1> y <p>).
    
    #return render_template("inicio.html", vuelo={"titulo": "Aerolinea aerolista"})
    return "<h1>¡Hola desde Flask! ✈</h1><p>El servidor de AeroLista está funcionando!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.</p>"


# ===== ENCENDER EL SERVIDOR =====
# Este bloque solo se ejecuta cuando corres el archivo con:  python app.py
# (si otro archivo lo importa, no se ejecuta).
if __name__ == "__main__":
    # debug=True → si guardas un cambio en un archivo .py, Flask se
    #              reinicia solo y además muestra los errores con detalle.
    # port=5050  → el "número de puerta" por donde escucha el servidor.
    #              La dirección completa será http://127.0.0.1:5050
    app.run(debug=True, port=5050)
