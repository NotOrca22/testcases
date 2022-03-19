import unittest
from substring import commonPermuatation

class TestStringMethods(unittest.TestCase):

    def runTest(self):
        self.assertEqual("acor", commonPermuatation("orca", "acro"))


if __name__ == '__main__':
    unittest.main()