from pyxtalcomp import XtalCompASE
import unittest

try:
    from ase.build import bulk
    available = True
    reason = ""
except ImportError as exc:
    available = False
    reason = str(exc)

class TestASEAtoms(unittest.TestCase):
    def test_fcc_bcc(self):
        if not available:
            self.skipTest(reason)
        s1 = bulk("Al", crystalstructure="fcc")
        s2 = bulk("Al", crystalstructure="bcc", a=4.05)
        s1 = s1 * (2, 2, 2)
        s2 = s2 * (2, 2, 2)
        comp = XtalCompASE()
        self.assertFalse(comp(s1, s2))
    
    def test_single_impurity(self):
        s1 = bulk("Al")
        s1 = s1 * (2, 2, 2)
        s1[0].symbol = "Mg"
        s2 = bulk("Al")
        s2 = s2 * (2, 2, 2)
        s2[3].symbol = "Mg"
        comp = XtalCompASE()
        self.assertTrue(comp(s1, s2))

if __name__ == "__main__":
    unittest.main()