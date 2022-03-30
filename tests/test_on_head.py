import unittest


class OnHeadTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(OnHeadTest, self).__init__(*args, **kwargs)
        self.head = [0, 0]
        self.body = []
        self.lenght = 0

    # Function use to keep body follow head
    def do_on_head(self, *args):
        self.body = self.body[-self.lenght :] + [self.head]

    def test_do_on_head_check_index_1(self):
        self.lenght = 3
        self.head = [5, 5]  # Moving up
        self.do_on_head()  # Move body follow head
        self.head = [5, 6]  # Moving up
        self.do_on_head()  # Move body follow head
        self.head = [5, 7]  # Moving up
        self.do_on_head()  # Move body follow head

        # Check Body on index 1
        result = self.body[1]
        except_result = [5, 6]

        self.assertEqual(result, except_result)

    def test_do_on_head_check_in_for_loop_check_last(self):
        self.lenght = 4
        for i in range(1, 10):
            self.head = [5, i]
            self.do_on_head()

        # End loop with head in position [5, 9]
        # Body:Lenght4:-->Head: [5, 5]->[5, 6]->[5, 7]->[5, 8]->[5, 9]
        # Last Body is [5, 5]
        result = self.body[0]  # Object: [body::] + [head]
        except_result = [5, 5]

        self.assertEqual(result, except_result)

    def test_do_on_head_zig_zag(self):
        self.lenght = 3
        self.head = [1, 1]  # -
        self.do_on_head()
        self.head = [1, 2]  # ^
        self.do_on_head()
        self.head = [2, 2]  # >
        self.do_on_head()
        self.head = [2, 3]  # ^
        self.do_on_head()
        self.head = [3, 3]  # >
        self.do_on_head()

        # Check Body Before head
        result = self.body[-1]
        except_result = [3, 3]

        self.assertEqual(result, except_result)

    def test_do_on_head_x_axis_check_last(self):
        self.lenght = 2
        self.head = [1, 1]  # -
        self.do_on_head()
        self.head = [2, 1]  # >
        self.do_on_head()
        self.head = [3, 1]  # >>
        self.do_on_head()

        # Check Body Before head
        result = self.body[0]
        except_result = [1, 1]

        self.assertEqual(result, except_result)
