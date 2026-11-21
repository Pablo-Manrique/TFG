import subprocess
from io import StringIO
from pathlib import Path
from typing import Optional
import numpy as np

ROOT_DIR = Path(__file__).resolve().parent
BUILD_DIR = ROOT_DIR / "build"

# TODO: Acutalmente no funcionan los parámetros de entrada
def ejecutar_simulacion(
    ejecutable: str,
    configuracion: Optional[dict[str, dict[str, float]]]
):
    ruta_exe = BUILD_DIR / ejecutable

    if not ruta_exe.exists():
        print(f"Error: No se encuentra el ejecutable {ruta_exe}")
        return None

    archivo_salida = "out.txt"
    ruta_salida = BUILD_DIR / archivo_salida

    comando = [str(ruta_exe)]

    print(f"Ejecutando: {' '.join(comando)}")
    result = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        cwd=BUILD_DIR,
    )

    if result.returncode != 0:
        print(f"Error en la simulacion:\n{result.stderr}")
        return None

    data = np.loadtxt(StringIO(result.stdout))
    resultado = {
        "tiempo": data[:, 0].tolist(),
        "v_soma": data[:, 1].tolist(),
    }
    if data.shape[1] >= 3:
        resultado["v_axon"] = data[:, 2].tolist()
    if data.shape[1] >= 4:
        resultado["p"] = data[:, 3].tolist()
    if data.shape[1] >= 5:
        resultado["h"] = data[:, 4].tolist()
    if data.shape[1] >= 6:
        resultado["n_gate"] = data[:, 5].tolist()

    print(f"Simulacion completada: {len(resultado['tiempo'])} puntos")
    return resultado