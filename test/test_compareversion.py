import unittest
from question_b import compareVersionString as cv

class TestPadStringLength(unittest.TestCase):
    def test_padStringZeroCase01(self):
        """ if version 1 is '1.0.1' and version2 = '1' make or reformat version2 to '1.0.0' before invoking the compareversion function\n """
        self.version = '1'
        self.version = self.version.split('.')
        self.length = 3
        self.padding = '0'
        self.assertCountEqual(cv.padStringZero(self.version, self.length, self.padding),['1', '0', '0'])
        print("\n In test_padStringZero01()")


    def test_padStringZeroCase02(self):
        """ if version 1 is '1.1' and version2 = '1' make or reformat version2 to '1.0' before invoking the compareversion function\n """
        self.version = '1'
        self.version = self.version.split('.')
        self.length = 2
        self.padding = '0'
        self.assertCountEqual(cv.padStringZero(self.version, self.length, self.padding),['1', '0'])
        print("\n In test_padStringZero02()")

class TestCompareVersion(unittest.TestCase):
    def test_compareVersion_different_length_Equal_version_case01(self):
        """ Compare version1 = '1.1.0' and version2 = '1.1'. it should return 0. The Two versions are equal \n """
        self.assertEqual(cv.compareVersion('1.1.0', '1.1'),0)
        print("\n In test_compareVersion_different_length_Equal_version_case01()")

    def test_compareVersion_Same_length_Equal_version_case02(self):
        """ Compare version1 = '1.1.0' and version2 = '1.1.0'. it should return 0. The Two versions are equal \n """
        self.assertEqual(cv.compareVersion('1.1.0', '1.1.0'),0)
        print("\n In test_compareVersion_Same_length_Equal_version_case02()")

    def test_compareVersion_different_length_first_bigger_version_case01(self):
        """ Compare version1 = '1.0.1' and version2 = '1'. it should return 1. Versions2 is smaller \n """
        self.assertEqual(cv.compareVersion('1.1.0', '1'),1)
        print("\n In test_compareVersion_different_length_first_bigger_version_case01()")

    def test_compareVersion_same_length_first_bigger_version_case02(self):
        """ Compare version1 = '2.0.1' and version2 = '2.0.0'. it should return 1. Versions2 is smaller \n """
        self.assertEqual(cv.compareVersion('2.0.1', '2.0.0'),1)
        print("\n In test_compareVersion_same_length_first_bigger_version_case02()")

    def test_compareVersion_same_length_first_bigger_version_case03(self):
        """ Compare version1 = '3' and version2 = '2'. it should return 1. Versions2 is smaller \n """
        self.assertEqual(cv.compareVersion('3', '2'),1)
        print("\n In test_compareVersion_same_length_first_bigger_version_case03()")

    def test_compareVersion_different_length_second_bigger_version_case01(self):
        """ Compare version1 = '1.1.0' and version2 = '1.1.1.3.0.0'. it should return -1. Versions1 is Smaller \n """
        self.assertEqual(cv.compareVersion('1.1.0', '1.1.1.3.0.0'),-1)
        print("\n In test_compareVersion_different_length_second_bigger_version_case01()")

    def test_compareVersion_same_length_second_bigger_version_case02(self):
        """ Compare version1 = '1.1.0.3.0.0' and version2 = '1.1.1.3.0.0'. it should return -1. Versions1 is Smaller \n """
        self.assertEqual(cv.compareVersion('1.1.0.3.0.0', '1.1.1.3.0.0'),-1)
        print("\n In test_compareVersion_same_length_second_bigger_version_case02()")

    def test_compareVersion_same_length_second_bigger_version_case03(self):
        """ Compare version1 = '4' and version2 = '7'. it should return -3. Versions1 is Smaller \n """
        self.assertEqual(cv.compareVersion('4', '7'),-3)
        print("\n In test_compareVersion_same_length_second_bigger_version_case03()")

    def test_compareVersion_raise_error_if_not_string_parameter01(self):
        """ Compare version1 = '4' and version2 = '. it should Attribute Error \n """
        with self.assertRaises(AttributeError): cv.compareVersion('4', 7)
        print("\n In test_compareVersion_raise_error_if_not_string_parameter01()")

    def test_compareVersion_raise_error_if_wrong_parameter02(self):
        """ Compare version1 = '4' and version2 = '. it should Attribute Error \n """
        with self.assertRaises(ValueError): cv.compareVersion('3.3.d.1', '3.c.4.a')
        print("\n In test_compareVersion_raise_error_if_wrong_parameter02()")

class TestcompareVersionDriver(unittest.TestCase):
        def test_compareVersionDriver_string_case01(self):
            """ Compare version1 = '1.1.3' and version2 =  '1.1.3' Version1 and version2 are equal \n """
            self.assertEqual(cv.compareVersionDriver('1.1.3', '1.1.3'),"'1.1.3' is same version as '1.1.3'")
            print("\n In test_compareVersionDriver_string_case01()")

        def test_compareVersionDriver_string_case02(self):
            """ Compare version1 = '2' and version2 = '3' Version2 is greater \n """
            self.assertEqual(cv.compareVersionDriver('2', '3'),"'2' is smaller than '3'")
            print("\n In test_compareVersionDriver_string_case02()")

        def test_compareVersionDriver_string_case03(self):
            """ Compare version1 = '1.2.4.0.0.1.0' and version2 = '1.2.4.0.0.1.0.0.0' Version1 is greater \n """
            self.assertEqual(cv.compareVersionDriver('1.2.4.0.0.1.0', '1.2.4.0.0.1.0.0.0'),"'1.2.4.0.0.1.0' is same version as '1.2.4.0.0.1.0.0.0'")
            print("\n In test_compareVersionDriver_string_case03()")

        def test_compareVersionDriver_string_case04(self):
            """ Compare version1 = '1.2.3.0.0.0.0.0.0' and version2 =  '1.2.3' Version1 and version2 are equal \n """
            self.assertEqual(cv.compareVersionDriver('1.2.3.0.0.0.0.0.0', '1.2.3'),"'1.2.3.0.0.0.0.0.0' is same version as '1.2.3'")
            print("\n In test_compareVersionDriver_string_case04()")

        def test_compareVersionDriver_string_case05(self):
            """ Compare version1 = '1.0' and version2 = '5.9.8.5.2' Version2 is greater \n """
            self.assertEqual(cv.compareVersionDriver('1.0', '5.9.8.5.2'),"'1.0' is smaller than '5.9.8.5.2'")
            print("\n In test_compareVersionDriver_string_case05()")

        def test_compareVersionDriver_string_case06(self):
            """ Compare version1 = '1.4.0.6.0.0' and version2 = '1.4.1.0.0.9.0.5' Version2 is greater \n """
            self.assertEqual(cv.compareVersionDriver('1.4.0.6.0.0', '1.4.1.0.0.9.0.5'),"'1.4.0.6.0.0' is smaller than '1.4.1.0.0.9.0.5'")
            print("\n In test_compareVersionDriver_string_case06()")

        def test_compareVersionDriver_string_case07(self):
            """ Compare version1 = '1.2.0.2.2.3.5.7.1' and version2 =  '1.2.1.0.0.1' Version2 is greater \n """
            self.assertEqual(cv.compareVersionDriver('1.2.0.2.2.3.5.7.1', '1.2.1.0.0.1'),"'1.2.0.2.2.3.5.7.1' is smaller than '1.2.1.0.0.1'")
            print("\n In test_compareVersionDriver_string_case07()")

        def test_compareVersionDriver_string_case08(self):
            """ Compare version1 = '5' and version2 = '1.0.0.0.0' Version1 is greater \n """
            self.assertEqual(cv.compareVersionDriver('5', '1.0.0.0.0'),"'1.0.0.0.0' is smaller than '5'")
            print("\n In test_compareVersionDriver_string_case08()")

        def test_compareVersionDriver_string_case09(self):
            """ Compare version1 = '1.4.1.0.0.0.0.0.0' and version2 = '1.4.0.6' Version1 is greater \n """
            self.assertEqual(cv.compareVersionDriver('1.4.1.0.0.0.0.0.0', '1.4.0.6'),"'1.4.0.6' is smaller than '1.4.1.0.0.0.0.0.0'")
            print("\n In test_compareVersionDriver_string_case09()")

        def test_compareVersionDriver_string_case10(self):
            """ Compare version1 = '1.2.1.0.0.0.1' and version2 = '1.2.0.2.9.0.1.2.1.2.3.5' Version1 is greater \n """
            self.assertEqual(cv.compareVersionDriver('1.2.1.0.0.0.1', '1.2.0.2.9.0.1.2.1.2.3.5'),"'1.2.0.2.9.0.1.2.1.2.3.5' is smaller than '1.2.1.0.0.0.1'")
            print("\n In test_compareVersionDriver_string_case10()")

        def test_compareVersionDriver_string_case11(self):
            """ Compare version1 = '1.4.0.6' and version2 = 1.4.1.0' Version2 is greater \n """
            self.assertEqual(cv.compareVersionDriver('1.4.0.6', '1.4.1.0'),"'1.4.0.6' is smaller than '1.4.1.0'")
            print("\n In test_compareVersionDriver_string_case11()")

        def test_compareVersionDriver_string_case12(self):
            self.assertEqual(cv.compareVersionDriver('1.2.0', '1.2.1'),"'1.2.0' is smaller than '1.2.1'")
            print("\n In test_compareVersionDriver_string_case12()")


        def test_compareVersionDriver_string_case13(self):
            """ Compare version1 = '1.2' and version2 = 2.3 it should Attribute Error \n """
            with self.assertRaises(AttributeError): cv.compareVersionDriver('1.2', 2.3)
            print("\n In test_compareVersionDriver_string_case13()")

        def test_compareVersionDriver_string_case14(self):
            """ Compare version1 = '1.2.c' and version2 = 1.b.1.a' it should Value Error \n """
            with self.assertRaises(ValueError): cv.compareVersionDriver('1.2.c', '1.b.1.a')
            print("\n In test_compareVersionDriver_string_case14()")
