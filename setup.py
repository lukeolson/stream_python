# python setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Cython Reference',
    ext_modules=cythonize("cython_ref.pyx"),
)
