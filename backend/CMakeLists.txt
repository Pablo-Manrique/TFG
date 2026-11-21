cmake_minimum_required(VERSION 3.14)
project(NeunBackendSim LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Descarga automáticamente la librería neun desde GitHub al hacer 'cmake ..'
include(FetchContent)
FetchContent_Declare(
    neun
    GIT_REPOSITORY https://github.com/GNB-UAM/Neun.git
    GIT_TAG master
)
FetchContent_MakeAvailable(neun)

# Añade los directorios de cabeceras de neun
include_directories(${neun_SOURCE_DIR}/include)

# Ejemplo de ejecutable (descomenta cuando añadas tu .cpp en src/)
# find_package(yaml-cpp REQUIRED)
# add_executable(sim_neurona src/sim_neurona.cpp)
# target_link_libraries(sim_neurona PRIVATE yaml-cpp)