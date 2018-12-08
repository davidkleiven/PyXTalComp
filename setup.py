from setuptools import setup, Extension

module1 = Extension( "pyxtalcomp_cpp", sources=["src/pyxtalcomp.cpp","src/xc_tools.cpp"],
include_dirs=["include"], extra_compile_args=['-std=c++11'], language="c++",
libraries=["XtalComp"])

setup(
    name="pyxtalcomp",
    ext_modules=[module1]
)
