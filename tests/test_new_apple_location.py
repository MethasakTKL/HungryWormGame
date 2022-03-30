import unittest


class NewAppleLocationTest(unittest.TestCase):

    # Unittest Section
    def do_new_apple_location(self):
        from random import randint

        COLS = 10
        ROWS = 10
        while True:
            new_apple = [randint(1, dim - 1) for dim in [COLS, ROWS]]
            if new_apple not in self.body and new_apple != self.apple:
                self.apple = new_apple
                return 

    def test_new_apple_location(self):
        self.body = [5, 5]
        self.apple = [10, 5]
        self.do_new_apple_location()
        apple1 = self.apple
        self.do_new_apple_location()
        apple2 = self.apple

        self.assertNotEqual(apple1, apple2)
