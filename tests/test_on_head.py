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

