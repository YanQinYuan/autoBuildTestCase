import unittest
from buildCase import varcharBuild

class TestAutoBuild(unittest.TestCase):
    def test_varcharBuild():
        self.assertEqual(len(varcharBuild()), 6)

if __name__ == '__main__':
    unittest.main()
