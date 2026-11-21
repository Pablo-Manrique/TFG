from io import BytesIO
import os
from typing import Optional
import matplotlib
matplotlib.use("Agg")  # Evita intentar abrir ventanas gráficas en el servidor
import matplotlib.pyplot as plt
from fastapi import FastAPI, HTTPException, Response
from simulaciones import ejecutar_simulacion

app = FastAPI(title="API de Simulación")

# Llamada POST para que se pueda usar el body
@app.post("/simular/{modelo}")
def lanzar_neurona(modelo: str, configuracion: Optional[dict[str, dict[str, float]]]):
    datos_n1m = ejecutar_simulacion(modelo, configuracion)
    if datos_n1m is None:
        raise HTTPException(
            status_code=500,
            detail="Error al ejecutar la simulación. Verifica que el ejecutable exista."
        )

    t = datos_n1m['tiempo']
    v_soma = datos_n1m['v_soma']
    v_axon = datos_n1m.get('v_axon', None)
    p = datos_n1m.get('p', None)
    h = datos_n1m.get('h', None)
    n_gate = datos_n1m.get('n_gate', None)

    fig, ax = plt.subplots(figsize=(14, 6))

    # Panel 1: Voltaje del Soma (plateau)
    ax.plot(t, v_soma, 'b-', linewidth=0.8, label='$V_S$ (soma)')
    ax.set_ylabel('$V_S$ (mV)', fontsize=12)
    ax.set_title('N1M: Compartimento Somatico', fontsize=13)
    ax.axhline(y=-67, color='gray', linestyle='--', alpha=0.5, label='$E_{leak}$')
    ax.axhline(y=-30, color='red', linestyle=':', alpha=0.5, label='$E_{ACh}$')
    ax.axvspan(200, 1800, alpha=0.1, color='green', label='Estimulo')
    ax.legend(loc='upper right', fontsize=9)
    ax.set_xlim([0, t[-1]])

    plt.tight_layout()

    # Volcar la gráfica en memoria y cerrar la figura para liberar RAM
    buf = BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)

    #TODO: Ahora mismo reenviamos la imagen, pero en un futuro será mejor hacer la gráfica desde Vue 
    # el objetivo es poder descargarte los resultados exactos y permitir más opciones en el frontend como ampliar o mover

    return Response(content=buf.getvalue(), media_type="image/png")