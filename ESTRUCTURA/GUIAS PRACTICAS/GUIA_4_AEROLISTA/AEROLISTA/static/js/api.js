// ================================================================
//  AeroLista ✈ · api.js — cómo HABLA la página con Flask
//  Cada función del objeto API hace un pedido (fetch) a una ruta
//  /api/... de app.py y devuelve el JSON que contesta Flask:
//     { ok: true,  datos: ..., mensaje: "...", avisos: [...] }
//     { ok: false, mensaje: "..." }
// ================================================================

const SEGUNDOS_DE_ESPERA = 6;      // si Flask tarda más que esto, nos rendimos

// async: esta función tarda (viaja por la red), así que trabaja "en segundo plano".
// Dentro de una función async podemos usar await = "espera aquí hasta que llegue".
async function pedir(url, metodo = "GET", cuerpo = null, espera = SEGUNDOS_DE_ESPERA) {
  // Un "controlador" nos permite CANCELAR el pedido si tarda demasiado
  const controlador = new AbortController();
  const reloj = setTimeout(() => controlador.abort(), espera * 1000);   // alarma en 6 s

  // Opciones del pedido: método (GET, POST, PUT, DELETE) y encabezados
  const opciones = { method: metodo, signal: controlador.signal, headers: {} };
  if (cuerpo !== null) {                                 // si hay datos para ENVIAR...
    opciones.headers["Content-Type"] = "application/json";   // ...avisamos que van en JSON
    opciones.body = JSON.stringify(cuerpo);              // objeto JS → texto JSON
  }

  try {                                                  // try: "intenta esto..."
    const respuesta = await fetch(url, opciones);       // 1. viaja a Flask y espera la respuesta
    return await respuesta.json();                       // 2. texto JSON → objeto de JavaScript
  } catch (error) {                                      // catch: "...y si algo falla, haz esto"
    if (error.name === "AbortError") {                   // sonó la alarma: tardó demasiado
      return { ok: false, error_codigo: true,
               mensaje: `Flask no respondió en ${espera} s. ¿Hay un bucle infinito? ` +
                        "Revisa que avances con actual = actual.next y reinicia Flask (Ctrl+C)." };
    }
    return { ok: false, error_codigo: true,              // no hubo conexión
             mensaje: "No hay conexión con Flask. ¿Está encendido? → python app.py" };
  } finally {                                            // finally: se ejecuta SIEMPRE al final
    clearTimeout(reloj);                                 // apagamos la alarma
  }
}

// El objeto API empieza vacío. Cada función se agrega como API.nombre = ...
const API = {};

// GET /api/vuelo → los datos del avión (filas, letras...)
API.vuelo = () => pedir("/api/vuelo");
