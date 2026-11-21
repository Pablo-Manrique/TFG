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

# Flags for the compiler
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2 -I/usr/local/include/neun")

# Executable
add_executable(HR src/HR.cpp)
add_executable(basic src/basic.cpp)
add_executable(synapse src/synapse.cpp)
add_executable(chemicalSynapse src/chemicalSynapse.cpp)
add_executable(linskerSynapse src/linskerSynapse.cpp)
add_executable(STDPSynapse src/STDPSynapse.cpp)
add_executable(HR-loadparams src/HR-loadparams.cpp)

# # Linking equivalent to LDLIBS = -lyaml-cpp
target_link_libraries(HR-loadparams yaml-cpp)
