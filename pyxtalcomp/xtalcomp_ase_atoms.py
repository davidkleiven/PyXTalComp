from pyxtalcomp_cpp import compare_xtalcomp
import numpy as np


class XtalCompASE(object):
    def __init__(self):
        pass

    def __call__(self, atom1, atom2, cart_tol=0.05, angle_tol=0.5, reduce_cell=False):
        """Compare two ASE atoms"""
        positions1 = atom1.get_scaled_positions()
        symbs1 = [atom.symbol for atom in atom1]
        cell1 = np.array(atom1.get_cell())

        positions2 = atom2.get_scaled_positions()
        symbs2 = [atom.symbol for atom in atom2]
        cell2 = np.array(atom2.get_cell())
        match = compare_xtalcomp(positions1,symbs1, cell1,
                  positions2, symbs2, cell2, cart_tol, angle_tol, reduce_cell)
        return match
