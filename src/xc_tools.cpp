#define NO_IMPORT_ARRAY
#include "import_npy_api.hpp"
#include "xc_tools.hpp"
#include <map>
#include <Python.h>
#include <iostream>

using namespace std;

void get_positions( PyObject *pos_raw, vector<XcVector> &xc_pos )
{
  char* format=NULL;
  PyObject *pos = PyArray_FROM_OTF(pos_raw, NPY_DOUBLE, NPY_ARRAY_IN_ARRAY );
  npy_intp* dims = PyArray_DIMS(pos);
  for (unsigned int site=0;site<dims[0];site++)
  {
    double x = *static_cast<double*>(PyArray_GETPTR2(pos,site,0));
    double y = *static_cast<double*>(PyArray_GETPTR2(pos,site,1));
    double z = *static_cast<double*>(PyArray_GETPTR2(pos,site,2));
    XcVector vec(x,y,z);
    xc_pos.push_back(vec);
  };
  Py_DECREF(pos);
}

void get_types(PyObject* symbs, vector<unsigned int> &types, map<string,unsigned int> &symb_lut)
{
  unsigned int size = PyList_Size(symbs);
  unsigned int next_id = 1;
  for ( auto iter=symb_lut.begin();iter!=symb_lut.end();++iter )
  {
    if ( iter->second >= next_id ) next_id = iter->second+1;
  }
  
  for (unsigned int i=0;i<size;i++ )
  {
    string symbol;
    #if PY_MAJOR_VERSION >= 3
      symbol = PyUnicode_AsUTF8(PyList_GetItem(symbs,i));
    #else
      symbol = PyString_AsString(PyList_GetItem(symbs,i));
    #endif
    if ( symb_lut.find(symbol) == symb_lut.end() )
    {
      // New symbol
      symb_lut[symbol] = next_id++;
    }
    types.push_back(symb_lut[symbol]);
  }
}
