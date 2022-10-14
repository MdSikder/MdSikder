import unittest
from structure2.Pages.test_TC01 import Home
from structure2.Pages.test_TC02 import Home2


class MyTestCase(unittest.TestCase):
    def suite(self):
        suite = unittest.TestSuite
        # Get all tests from TestClass1 and TestClass2
        tc1 = unittest.TestLoader().loadTestsFromTestCase(Home)
        tc2 = unittest.TestLoader().loadTestsFromTestCase(Home2)

        # Create a test suite combining TestClass1 and TestClass
        smokeTest = unittest.TestSuite([tc1, tc2])
        unittest.TextTestRunner(verbosity=2).run(smokeTest)
        return suite


if __name__ == '__main__':
    unittest.main()
