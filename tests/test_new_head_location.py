import unittest


class NewHeadLocationTest(unittest.TestCase):

    # Unittest Section
    def do_new_head_location(self):
        from random import randint

        COLS = 10
        ROWS = 10
        new_head = [randint(2, dim - 2) for dim in [COLS, ROWS]]

        return new_head

    def test_new_head_location(self):
        head0 = [0, 0]  # Default Value of head pos in game
        head1 = self.do_new_head_location()  # Starting random head pos

        self.assertNotEqual(head0, head1)
