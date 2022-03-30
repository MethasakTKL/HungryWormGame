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
        head1 = self.do_new_head_location()
        head2 = self.do_new_head_location()

        self.assertIsNot(head1, head2)
