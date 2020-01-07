import unittest
from GoEngine import *

# A unit test file for GoEngine.py
class TestGo(unittest.TestCase):
    """Test Go, the main class"""

    def test_get_dimension(self):
        """Test get_dimension and initialization"""
        sample_game = Go(8)
        self.assertEqual(8,sample_game.get_dimension())

    def test_get_neighbor(self):
        """Test get_neighbor of a certain board"""
        sample_game = Go(4)
        self.assertEqual([[1,0],[0,1]],sample_game.get_neighbor([0,0]))

if __name__ == '__main__':
    unittest.main()