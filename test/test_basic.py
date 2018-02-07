import unittest
import sys
sys.path.append('../')
from ..autoBuildCase import buildCase


class TestAutoBuild(unittest.TestCase):
    def test_varcharBuild():
        self.assertEqual(len(varcharBuild()), 6)

if __name__ == '__main__':
    unittest.main()
