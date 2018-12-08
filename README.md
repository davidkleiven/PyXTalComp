# PyXTalComp
![Build status](https://travis-ci.org/davidkleiven/PyXTalComp.svg?branch=master)
Python interface to the XTalComp code

# Installation
First compile and install a **shared** library version of
[XtalComp](https://github.com/allisonvacanti/XtalComp).
Remember to compile with **-fPIC**.
Then install with
```bash
env CC=g++ pip install ./ --user
```
the **--user** argument is optional.

# Usage
To use the interface
```Python
from pyxtalcomp_cpp import compare_xtalcomp
import numpy as np

# Positions with scaled coordinates of the systems
# See also the documentation of XtalComp
positions1 = np.array([[0.1,0.2,0.3],[0.2,0.8,0.9]])
positions2 = np.array([[-0.1,0.6,0.7],[0.1,0.8,0.1]])

# The atomic symbols are placed in a list
symbs1 = ["Zn","Ti"]
symbs2 = ["Ti","Zn"]

# Specify unit cells. NumPy arrays, but the format is the same as in
# XtalComp
cell1 = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
cell1 = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])

# Toleracne parameters (See XtalComp documentation)
cart_tol = 0.05
angle_tol = 0.25

# Should XtalComp use spglib to reduce the systems?
reduce_cell = False

# Match is True if the structures are similar and False otherwise
match = compare_xtalcomp(positions1,symbs1, cell1,
          positions2, symbs2, cell2, cart_tol, angle_tol, reduce_cell)
```

# Compare two ASE Atoms objects
```python
from pyxtalcomp import XtalCompASE
from ase.build import bulk

# Create Aluminium FCC atoms
s1 = bulk("Al")
s1 = s1 * (2, 2, 2)

# Insert Mg impurity
s1[0].symbol = "Mg"
s2 = bulk("Al")
s2 = s2 * (2, 2, 2)

# Insert Mg impurity on a different place
s2[3].symbol = "Mg"
comp = XtalCompASE()

# Check if the two atoms objects a symmetrically
# equivalen (should evaluate to True)
match = comp(s1, s2)
```
