<script setup>
import { ref, computed } from 'vue'
import Simulador from '../components/Simulador.vue'
import VentanaFlotante from '@/components/VentanaFlotante.vue';

const MAX_EN_PANTALLA = 2
const modelos = ref([])

const estaLleno = () => {
  return modelos.value.filter((m) => !m.flotante).length >= MAX_EN_PANTALLA
}

const modelosPantalla = computed(() => modelos.value.filter((m) => !m.flotante))
const modelosFlotantes = computed(() => modelos.value.filter((m) => m.flotante))

const anadirModelo = (nombreModelo) => {
  modelos.value.push({
    id: Date.now() + Math.random(),
    nombre: nombreModelo,
    flotante: estaLleno()
  })
}

const manejarQuitarModelo = async (modelo) => {
  // Invoca el método expuesto con defineExpose en ModelosView.vue
  modelos.value = modelos.value.filter((m) => m.id !== modelo.id)
}

const manejarPopUp = async (modelo) => {
  // Invoca el método expuesto con defineExpose en ModelosView.vue
  if (modelo.flotante == false) {
    modelo.flotante = true
  } else {
    if(!estaLleno())
      modelo.flotante = false
  }
}

// Expone el método hacia el componente padre (App.vue)
defineExpose({
  anadirModelo
})

</script>

<template>
  <div class="contenedor-simuladores">
    <div v-for="modelo in modelosPantalla" :key="modelo.id" class="bloque-simulador">
      <Simulador :modelo="modelo" @quitar-modelo="manejarQuitarModelo" @cambiar-pop="manejarPopUp"/>
    </div>

    <VentanaFlotante v-for="modelo in modelosFlotantes" :key="modelo.id">
      <Simulador :modelo="modelo" @quitar-modelo="manejarQuitarModelo" @cambiar-pop="manejarPopUp"/>
    </VentanaFlotante>
  </div>
</template>

<style scoped>
.contenedor-simuladores {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.bloque-simulador {
  flex: 1 0 calc(50% - 0.5rem);
  min-height: calc(50% - 0.5rem);
  max-height: 100%;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  border-color: black;
}
</style>