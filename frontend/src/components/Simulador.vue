<script setup>
const props = defineProps({
  modelo: {
    type: Object,
    required: true
  }
})

function eliminarModelo() {
  emit('quitar-modelo', props.modelo)
}

function sacarModelo() {
  emit('cambiar-pop', props.modelo)
}


const emit = defineEmits(['quitar-modelo', 'cambiar-pop'])
</script>

<template>
  <div class="simulador-container">
    <aside class="barra-params">
      <h2 class="titulo-params">Parametros</h2>
      <ul class="lista-params">
        <li>Parámetro 1</li>
        <li>Parámetro 2</li>
        <li>Parámetro 3</li>
        <li>Parámetro 4</li>
      </ul>

      <button type="button" class="btn-simular">Simular</button>
    </aside>
    <section class="zona-graficas">
      <header class="cabecera-graficas">
        <button type="button" class="btn-cerrar" title="Cerrar simulación" @click="eliminarModelo">
          ✕
        </button>
        <button type="button" class="btn-cerrar" @click="sacarModelo">
          <span class="material-icons">{{props.modelo.flotante ? 'open_in_new_down' : 'open_in_new'}}</span>
        </button>
      </header>

      <div class="placeholder-graficas">
        TODO: Aquí se mostrarán las gráficas
      </div>
    </section>
  </div>
</template>

<style scoped>
.simulador-container {
  display: flex;
  width: 100%;
  flex: 1;
  box-sizing: border-box;
  border: 1px solid #000000;
  padding: 10px;
  overflow: hidden;
  background-color: #ffffff;
}

.barra-params {
  background-color: #c8d1d9;
  max-width: 25%;
  width: 220px;
  min-width: 180px;
  padding: 1rem;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

.titulo-params {
  margin: 0 0 0.75rem 0;
  font-size: 1.15rem;
}

.btn-simular {
  margin-top: auto;      /* Lo mantiene abajo del todo */
  align-self: center;    /* Lo centra horizontalmente sin afectar a los demás elementos */
  width: 90%;    /* Se ajusta al texto sin desbordar la barra lateral */
  padding: 0.5rem 1.5rem;
  background-color: #00a65c;
  color: #000000;
  font-weight: 600;
  text-align: center;
  text-decoration: none;
  border: 1px solid #00a65c;
  border-radius: 51px;
  cursor: pointer;
}

.btn-simular:hover {
  background-color: #008f4f;
  border-color: #008f4f;
}

.zona-graficas {
  flex: 1;
  padding: 1rem 1.25rem;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

.cabecera-graficas {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.titulo-modelo {
  margin: 0;
  font-size: 1.1rem;
}

.btn-cerrar {
  background-color: #c8d1d9;
  color: #000000;
  border: none;
  width: 28px;
  height: 28px;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.placeholder-graficas {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px dashed #cbd5e1;
  border-radius: 8px;
  color: #64748b;
}
</style>