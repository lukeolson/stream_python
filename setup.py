# python setup.py build_ext --inplace
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import os

os.environ["CC"] = "/usr/local/bin/gcc-5"

module_ref = Extension("cython_ref",
                       ["cython_ref.pyx"],
                       extra_compile_args=["-O3", "-march=native"])

module_omp = Extension("cython_omp",
                       ["cython_omp.pyx"],
                       extra_compile_args=["-O3", "-march=native", "-fopenmp"],
                       extra_link_args=["-fopenmp"])

setup(name="cython_stream",
      cmdclass={"build_ext": build_ext},
      ext_modules=[module_ref, module_omp])
