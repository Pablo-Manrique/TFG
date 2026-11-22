<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView } from "vue-router";
import BarraSuperior from "./components/BarraSuperior.vue";
import HomeView from "./views/HomeView.vue"
import AboutView from './views/AboutView.vue';

const vista = ref(null)
const simulacion = ref(true)

const manejarAnadirModelo = async (nombreModelo) => {
  // Invoca el método expuesto con defineExpose en ModelosView.vue
  vista.value?.anadirModelo(nombreModelo)
  simulacion.value = true
}

const manejarVista = async (sim) => {
  // Invoca el método expuesto con defineExpose en ModelosView.vue
  simulacion.value = sim
}
</script>

<template>
  <div class="app-layout">
    <BarraSuperior @anadir-modelo="manejarAnadirModelo" @cambiar-vista="manejarVista"/>

    <main class="main-content">
      <HomeView v-show="simulacion" ref="vista" />
      <AboutView v-show="!simulacion" />
    </main>
  </div>
</template>

<style scoped>
.app-layout {
  height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  width: 100%;
  margin: 0 auto;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}
</style>
