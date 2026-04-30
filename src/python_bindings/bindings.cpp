#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h> // REQUIRED: Maps std::function to Python Callable
#include "othello_engine.cpp"

namespace py = pybind11;

PYBIND11_MODULE(othello_core, m) {
    m.doc() = "C++ Othello Core Wrapper with Neural Callbacks";

    py::class_<OthelloEngine>(m, "OthelloEngine")
     .def(py::init<>())
     .def("search_baseline", &OthelloEngine::searchBaseline)
     .def("search_enhanced", &OthelloEngine::searchEnhanced,
          py::arg("b"), py::arg("w"), py::arg("depth"), py::arg("alpha"), py::arg("beta"),
          py::arg("isBlack"), py::arg("ply"), py::arg("hash"), py::arg("nnEval") = nullptr);
}