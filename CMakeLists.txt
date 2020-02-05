cmake_minimum_required(VERSION 3.14)

project(exo LANGUAGES CXX VERSION 0.1.0)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set_property(GLOBAL PROPERTY USE_FOLDERS ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

option(EXO_DOWNLOAD_PYBIND11 "Download Pybind11" ON)

if(EXO_DOWNLOAD_PYBIND11)
  include(FetchContent)

  FetchContent_Declare(pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG v2.4.3
  )

  FetchContent_MakeAvailable(pybind11)
else()
  find_package(pybind11 REQUIRED)
endif()

option(EXO_DOWNLOAD_SPAN_LITE "Download span-lite" ON)

if(EXO_DOWNLOAD_SPAN_LITE)
  include(FetchContent)

  FetchContent_Declare(span-lite
    GIT_REPOSITORY https://github.com/martinmoene/span-lite.git
    GIT_TAG master
  )

  FetchContent_MakeAvailable(span-lite)
else()
  find_package(span-lite REQUIRED)
endif()

add_library(exo STATIC)

target_sources(exo
  PRIVATE
    ${PROJECT_SOURCE_DIR}/src/exo/exo.cpp
    ${PROJECT_SOURCE_DIR}/src/exo/exo.hpp
    ${PROJECT_SOURCE_DIR}/src/exo/matrix_span.hpp
)

set_target_properties(exo
  PROPERTIES
    POSITION_INDEPENDENT_CODE ON
)

target_include_directories(exo
  PUBLIC
    ${PROJECT_SOURCE_DIR}/src
)

target_link_libraries(exo
  PUBLIC
    nonstd::span-lite
)

pybind11_add_module(exopy ${PROJECT_SOURCE_DIR}/src/exopy/exopy.cpp)

target_include_directories(exopy
  PRIVATE
    ${PROJECT_SOURCE_DIR}/src
)

target_link_libraries(exopy
  PRIVATE
    exo
)

install(TARGETS exopy
  EXPORT exopyTargets
  LIBRARY DESTINATION .
  ARCHIVE DESTINATION .
  RUNTIME DESTINATION .
  INCLUDES DESTINATION .
)

option(EXO_ENABLE_PACKAGING "Enabling packaging for exopy" ON)

if(EXO_ENABLE_PACKAGING)
  include(CPack)
endif()
