import unittest

from unittest.mock import patch


class NewAppleLocationTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(NewAppleLocationTest, self).__init__(*args, **kwargs)
        self.apple = []
        self.body = []
        self.COLS = 10
        self.ROWS = 10

    # Unittest Section
    def do_new_apple_location(self):
        from random import randint

        while True:
            new_apple = [randint(1, dim - 1) for dim in [self.COLS, self.ROWS]]
            if new_apple not in self.body and new_apple != self.apple:
                self.apple = new_apple
                return

    def test_new_apple_location(self):
        self.do_new_apple_location()
        apple1 = self.apple
        self.do_new_apple_location()
        apple2 = self.apple

        self.assertNotEqual(apple1, apple2)

    def test_new_apple_3_times(self):
        self.do_new_apple_location()
        apple1 = self.apple
        self.do_new_apple_location()
        apple2 = self.apple
        self.do_new_apple_location()
        apple3 = self.apple

        self.assertNotEqual(apple1, apple2, apple3)

    def test_new_apple_every_place_in_map(self):
        self.COLS = 2
        self.ROWS = 3  # Resize map 2x3
        self.do_new_apple_location()  # 1/6
        self.do_new_apple_location()  # 2/6
        self.do_new_apple_location()  # 3/6
        self.do_new_apple_location()  # 4/6
        apple1 = self.apple
        self.do_new_apple_location()  # 5/6
        apple2 = self.apple
        self.do_new_apple_location()  # 6/6
        apple3 = self.apple
        # Now the whole map is full of apples.

        self.assertNotEqual(apple1, apple2, apple3)

    @patch(
        "tests.test_new_apple_location.NewAppleLocationTest.do_new_apple_location",
        return_value=[5, 5],
    )
    def test_new_apple_mock_location(self, do_new_apple_location):
        result = do_new_apple_location()
        expect_result = [5, 5]

        self.assertEqual(result, expect_result)

