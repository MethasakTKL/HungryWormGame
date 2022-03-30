import unittest


class CheckInBoundTest(unittest.TestCase):
    def check_in_bounds(self, position):
        COLS = 10
        ROWS = 10
        if all(0 <= position[x] < dim for x, dim in enumerate([COLS, ROWS])):
            return True
        else:
            return False


    def test_in_bounds(self):
        position = [10, 10]
        result = self.check_in_bounds(position)
        
        self.assertFalse(result)
    
    def test_not_in_bounds(self):
        position = [5, 5]
        result = self.check_in_bounds(position)

        self.assertTrue(result)