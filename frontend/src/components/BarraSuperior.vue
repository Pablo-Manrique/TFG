<script setup>
import { ref } from 'vue';

const isOpen = ref(false);
// TODO: Modificar por un JSON cargado con cada modelo posible
const options = ['basic', 'HR-loadparams']

function seleccionarModelo(option) {
  isOpen.value = false;
  emit('anadir-modelo', option)
}

function cambiarVista(option) {
  isOpen.value = false;
  emit('cambiar-vista', option)
}

const emit = defineEmits(['anadir-modelo', 'cambiar-vista'])
</script>

<template>
  <header class="navbar">
    <img src="/images/logo.png" alt="Logo Neun" class="logo" />
    <nav class="nav-links">
      <button class="nav-button" @click="cambiarVista(true)">Simulaciones</button>
      <div class="dropdown-container">
        <button type="button" class="nav-button" @click="isOpen = !isOpen">
          Modelos
        </button>

        <ul v-if="isOpen" class="dropdown-menu">
          <li v-for="option in options" :key="option">
            <button type="button" class="dropdown-item" @click="seleccionarModelo(option)">
              {{ option }}
            </button>
          </li>
        </ul>
      </div>  
      <button class="nav-button">Cargar Modelo</button>
      <button class="nav-button" @click="cambiarVista(false)">Tutorial</button>
    </nav>
    <!-- TODO: Modificar por la ayuda de navegacion si se acaba haciendo -->
    <img src="/images/logo.png" alt="Logo Neun" class="logo" />
  </header>
</template>

<style scoped>
.navbar {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  padding: 0.75rem 2rem;
  background-color: #72e7b3;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}

.logo-link {
  display: flex;
  align-items: center;
}

.logo {
  height: 42px;
  width: 42px;
  display: block;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: clamp(1rem, 4vw, 5rem);
}

.nav-button {
  text-decoration: none;
  background-color: #00a65c;
  /* Color de fondo del botón */
  color: #000000;
  /* Color del texto */
  font-weight: 600;
  text-align: center;
  width: 200px;
  padding: 0.5rem 1rem;
  border-radius: 51px;
  border-color: #00a65c;
}



/* 1. El contenedor sirve de ancla */
.dropdown-container {
  position: relative;
}

.dropdown-btn {
  padding: 8px 16px;
  cursor: pointer;
}

/* 2. El menú flota por encima de todo */
.dropdown-menu {
  position: absolute;
  top: 90%;
  /* Se coloca justo debajo del botón */
  left: 0;
  /* Alineado a la izquierda (usa right: 0 para alinear a la derecha) */
  z-index: 1000;
  /* Asegura que quede por encima de otros elementos */
  margin: 4px 0 0 0;
  padding: 4px 0;
  list-style: none;
  background-color: #72e7b3;
  min-width: 200px;
  border-radius: 20px;
}

.dropdown-item {
  width: 100%;
  padding: 8px 16px;
  text-align: left;
  background: none;
  border: none;
  cursor: pointer;
}
</style>
