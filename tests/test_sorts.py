import unittest

from src.sorts import (
    bubble_sort,
    selection_sort
)

class TestSortMethods(unittest.TestCase):
    def test_bubble_sort(self):
        # Arrange
        original = [5, 3, 9, 1, 7]
        expected = [1, 3, 5, 7, 9]
        
        # Act
        actual = bubble_sort(original)
    
        # Assert
        self.assertEqual(expected, actual)

    def test_selection_sort(self):
        # Arrange
        original = [54, 32, 87, 98]
        expected = [32, 54, 87, 99]
        
        # Act
        actual = selection_sort(original)
    
        # Assert
        self.assertEqual(expected, actual)
