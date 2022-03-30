import unittest


class CheckInBoundTest(unittest.TestCase):
    def check_in_bounds(self, position):
        COLS = 10
        ROWS = 10
        if all(0 <= position[x] < dim for x, dim in enumerate([COLS, ROWS])):
            return True
        else:
            return False


    def test_in_bounds_10_10(self):
        position = [10, 10]
        result = self.check_in_bounds(position)
        
        self.assertFalse(result)
    
    def test_not_in_bounds_5_5(self):
        position = [5, 5]
        result = self.check_in_bounds(position)

        self.assertTrue(result) 
    
    def test_in_bounds_20_20(self):
        position = [20, 20]
        result = self.check_in_bounds(position)

        self.assertFalse(result)
    
    def test_in_bounds_m1_m1(self):
        position = [-1, -1]
        result = self.check_in_bounds(position)

        self.assertFalse(result)