#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "othello_engine.cpp"

namespace py = pybind11;

PYBIND11_MODULE(othello_core, m) {
    py::class_<OthelloEngine>(m, "OthelloEngine")
      .def(py::init<>())
      .def("minimax_baseline", &OthelloEngine::minimax_baseline)
      .def("minimax_enhanced", &OthelloEngine::minimax_enhanced);
}