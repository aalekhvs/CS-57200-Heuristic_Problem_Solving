cmake_minimum_required(VERSION 3.14)
project(OthelloCore)

set(CMAKE_CXX_STANDARD 17)

# Fix the CMP0148 warning by forcing pybind11 to use modern CMake Python discovery
set(PYBIND11_FINDPYTHON ON)

# Find PyBind11
find_package(pybind11 REQUIRED)

# Create the Python module
pybind11_add_module(othello_core src/python_bindings/bindings.cpp)

# Include the engine headers
target_include_directories(othello_core PRIVATE src/engine)

# --- Fetch GoogleTest Automatically ---
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
# --------------------------------------

# Add GTest for tests
enable_testing()
add_executable(engine_tests tests/engine_tests.cpp)

# Link the automatically downloaded gtest_main library
target_link_libraries(engine_tests PRIVATE gtest_main)