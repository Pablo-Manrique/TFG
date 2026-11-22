<script setup>
import { ref } from 'vue'

defineProps({
    titulo: {
        type: String,
        default: 'Ventana de modelo'
    }
})

const emit = defineEmits(['cerrar'])

const minimizada = ref(false)

// Posición inicial (esquina inferior derecha)
const pos = ref({
    x: window.innerWidth - 440,
    y: window.innerHeight - 360
})

let arrastrando = false
let offset = { x: 0, y: 0 }

const iniciarArrastre = (e) => {
    arrastrando = true
    offset = {
        x: e.clientX - pos.value.x,
        y: e.clientY - pos.value.y
    }
    window.addEventListener('mousemove', mover)
    window.addEventListener('mouseup', soltar)
}

const mover = (e) => {
    if (!arrastrando) return
    pos.value = {
        x: Math.max(0, Math.min(window.innerWidth - 320, e.clientX - offset.x)),
        y: Math.max(0, Math.min(window.innerHeight - 45, e.clientY - offset.y))
    }
}

const soltar = () => {
    arrastrando = false
    window.removeEventListener('mousemove', mover)
    window.removeEventListener('mouseup', soltar)
}
</script>

<template>
    <Teleport to="body">
        <aside class="ventana-flotante" :class="{ minimizada }" :style="{ left: `${pos.x}px`, top: `${pos.y}px` }">
            <!-- Barra superior arrastrable -->
            <header class="ventana-cabecera" @mousedown="iniciarArrastre">
                <span class="ventana-titulo">{{ titulo }}</span>

                <div class="ventana-controles" @mousedown.stop>
                    <button type="button" class="btn-control" :title="minimizada ? 'Restaurar' : 'Minimizar'"
                        @click="minimizada = !minimizada">
                        {{ minimizada ? '□' : '—' }}
                    </button>
                    <button type="button" class="btn-control btn-cerrar" title="Cerrar" @click="emit('cerrar')">
                        ✕
                    </button>
                </div>
            </header>

            <!-- v-show mantiene vivos los inputs y datos internos aunque minimices -->
            <div v-show="!minimizada" class="ventana-cuerpo">
                <slot />
            </div>
        </aside>
    </Teleport>
</template>

<style scoped>
.ventana-flotante {
    position: fixed;
    width: 420px;
    max-height: 75vh;
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 10px;
    box-shadow: 0 12px 28px rgba(15, 23, 42, 0.18);
    display: flex;
    flex-direction: column;
    z-index: 900;
    overflow: hidden;
}

.ventana-flotante.minimizada {
    width: 280px;
    height: auto;
}

.ventana-cabecera {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.6rem 0.9rem;
    background-color: #00a65c;
    color: #ffffff;
    font-weight: 600;
    cursor: grab;
    user-select: none;
}

.ventana-cabecera:active {
    cursor: grabbing;
}

.ventana-controles {
    display: flex;
    gap: 0.35rem;
}

.btn-control {
    background: rgba(255, 255, 255, 0.2);
    border: none;
    color: #ffffff;
    width: 24px;
    height: 24px;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
}

.btn-control:hover {
    background: rgba(255, 255, 255, 0.35);
}

.btn-cerrar:hover {
    background: #dc2626;
}

.ventana-cuerpo {
    padding: 1rem;
    overflow-y: auto;
    flex: 1;
}
</style>