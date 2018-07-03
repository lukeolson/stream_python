#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

void copy(const py::array_t<double> &a,
                py::array_t<double> &c)
{
    auto ra = a.unchecked();
    auto rc = c.mutable_unchecked();
    for (ssize_t i = 0; i < ra.shape(0); i++)
    {
        rc[i] = ra[i];
    }
}

void scale(      py::array_t<double> &b,
           const py::array_t<double> &c,
           const double scalar)
{
    auto rb = b.mutable_unchecked();
    auto rc = c.unchecked();
    for (ssize_t i = 0; i < rc.shape(0); i++)
    {
        rb[i] = scalar * rc[i];
    }
}

void add(const py::array_t<double> &a,
         const py::array_t<double> &b,
               py::array_t<double> &c)
{
    auto ra = a.unchecked();
    auto rb = b.unchecked();
    auto rc = c.mutable_unchecked();
    for (ssize_t i = 0; i < rc.shape(0); i++)
    {
        rc[i] = ra[i] + rb[i];
    }
}

void triad(      py::array_t<double> &a,
           const py::array_t<double> &b,
           const py::array_t<double> &c,
           const double scalar)
{
    auto ra = a.mutable_unchecked();
    auto rb = b.unchecked();
    auto rc = c.unchecked();
    for (ssize_t i = 0; i < rc.shape(0); i++)
    {
        ra[i] = rb[i] + scalar * rc[i];
    }
}

PYBIND11_MODULE(pybind11_ref, m) {
    m.doc() = R"pbdoc(Pybind11 bindings)pbdoc";
    m.def("copy", &copy,
          py::arg("a").noconvert(),
          py::arg("c").noconvert());
    m.def("scale", &scale,
          py::arg("b").noconvert(),
          py::arg("c").noconvert(),
          py::arg("scalar").noconvert());
    m.def("add", &add,
          py::arg("a").noconvert(),
          py::arg("b").noconvert(),
          py::arg("c").noconvert());
    m.def("triad", &triad,
          py::arg("a").noconvert(),
          py::arg("b").noconvert(),
          py::arg("c").noconvert(),
          py::arg("scalar").noconvert());
}
