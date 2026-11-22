// ================================================================
//  AeroLista ✈ · main.js  —  el "director de orquesta"
//  Versión 2: pide a Flask los datos del vuelo.
// ================================================================

// 🆕 ESTADO: la "memoria" de la página. Aquí guardamos lo que ya sabemos.
const estado = {
  vuelo: null,        // los datos del avión (llegan de /api/vuelo)
};

// 🆕 iniciar() arranca la aplicación. Es async porque espera a Flask.
async function iniciar() {
  const r = await API.vuelo();            // pide /api/vuelo y ESPERA la respuesta

  if (!r.ok) {                            // ! significa "no": si la respuesta NO fue ok...
    $("#pie").textContent = "❌ " + r.mensaje;
    return;                               // ...mostramos el error y salimos
  }

  estado.vuelo = r.datos;                 // guardamos el diccionario del vuelo
  console.log("Datos del vuelo:", estado.vuelo);   // míralo en la consola (F12)

  // Las comillas invertidas ` ` permiten meter variables con ${ }
  $("#pie").textContent = `✅ Flask envió el vuelo ${estado.vuelo.codigo}: ` +
                          `${estado.vuelo.filas} filas, de ${estado.vuelo.origen} a ${estado.vuelo.destino}`;
}

iniciar();    // ¡arranca!
