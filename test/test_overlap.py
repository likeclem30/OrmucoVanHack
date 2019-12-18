import unittest
from question_a import overlap as ol 

class TestOverlap(unittest.TestCase):
    def test_linesOverlap01(self):
        self.assertTrue(ol.linesOverlap((1,5),(2,6)))

    def test_linesOverlap02(self):
        self.assertFalse(ol.linesOverlap((1,5),(6,8)))

    def test_linesOverlap03(self):
        with self.assertRaises(TypeError): ol.linesOverlap(('1','5'),(6,8))
        print("\n In test_linesOverlap03")

    def test_linesOverlap04(self):
        """ it should TypeError \n """
        with self.assertRaises(TypeError): ol.linesOverlap((1),(6,8))
        print("\n In test_linesOverlap04")

    def test_linesOverlap05(self):
        """ it should TypeError \n """
        with self.assertRaises(TypeError): ol.linesOverlap(1,(6,8))
        print("\n In test_linesOverlap05")

    def test_linesOverlap06(self):
        """ it should TypeError \n """
        with self.assertRaises(TypeError): ol.linesOverlap(1,(6))
        print("\n In test_linesOverlap06")

    def test_linesOverlap07(self):
        """ it should TypeError \n """
        with self.assertRaises(TypeError): ol.linesOverlap((1,5),(3))
        print("\n In test_linesOverlap07")
