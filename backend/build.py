import os
import subprocess
from pathlib import Path

# Calcula las rutas dinámicamente respecto a la ubicación de este archivo
ROOT_DIR = Path(__file__).resolve().parent
BUILD_DIR = ROOT_DIR / "build"


def compilar_proyecto(forzar_cmake: bool = False) -> bool:
    """
    Crea la carpeta build si no existe, configura el proyecto con CMake
    y compila los ejecutables con make.
    """
    # 1. Crear carpeta build si no existe
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Ejecutar 'cmake ..' si aún no se ha generado el Makefile o si se fuerza
    makefile_path = BUILD_DIR / "Makefile"
    if not makefile_path.exists() or forzar_cmake:
        print("Configurando proyecto con CMake...")
        cmake_res = subprocess.run(
            ["cmake", ".."],
            cwd=BUILD_DIR,
            capture_output=True,
            text=True,
        )
        if cmake_res.returncode != 0:
            print(f"Error en CMake:\n{cmake_res.stderr}")
            return False

    # 3. Ejecutar 'make' usando los núcleos disponibles
    nucleos = os.cpu_count() or 2
    print(f"Compilando proyecto con make -j{nucleos}...")
    make_res = subprocess.run(
        ["make", f"-j{nucleos}"],
        cwd=BUILD_DIR,
        capture_output=True,
        text=True,
    )
    if make_res.returncode != 0:
        print(f"Error de compilación:\n{make_res.stderr}")
        return False

    print("Compilación exitosa.")
    return True


if __name__ == "__main__":
    exito = compilar_proyecto()
    if not exito:
        exit(1)