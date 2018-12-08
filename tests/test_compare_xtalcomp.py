from pyxtalcomp_cpp import compare_xtalcomp
import numpy as np
import unittest


class TestCompareXtalComp(unittest.TestCase):
    def test_equal(self):
        # Positions with scaled coordinates of the systems
        # See also the documentation of XtalComp
        positions1 = np.array([[0.1,0.2,0.3],[0.2,0.8,0.9]])
        positions2 = np.array([[-0.1,0.6,0.7],[0.1,0.8,0.1]])

        # The atomic symbols are placed in a list
        symbs1 = ["Zn","Ti"]
        symbs2 = ["Ti","Zn"]

        # Specify unit cells. NumPy arrays, but the format is the same as in
        # XtalComp
        cell1 = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]], dtype=np.float64)
        cell2 = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]], dtype=np.float64)

        # Toleracne parameters (See XtalComp documentation)
        cart_tol = 0.05
        angle_tol = 0.25

        # Should XtalComp use spglib to reduce the systems?
        reduce_cell = False

        # Match is True if the structures are similar and False otherwise
        match = compare_xtalcomp(positions1, symbs1, cell1,
                positions2, symbs2, cell2, cart_tol, angle_tol, reduce_cell)
        self.assertFalse(match)

if __name__ == "__main__":
    unittest.main()