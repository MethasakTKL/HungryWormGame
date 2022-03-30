import unittest

COLS = 10
ROWS = 10

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"

direction_values = {LEFT: [-1, 0], RIGHT: [1, 0], UP: [0, 1], DOWN: [0, -1]}


class MoveTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MoveTest, self).__init__(*args, **kwargs)
        self.head = [0, 0]
        self.body = []
        self.lenght = 0
        self.apple = []

    def do_move(self, *args):
        self.body = self.body[-self.lenght :] + [self.head]
        new_pos = [sum(x) for x in zip(self.head, direction_values[self.direction])]

        if (
            not all(0 <= new_pos[x] < d for x, d in enumerate([COLS, ROWS]))
            or new_pos in self.body
        ):
            return False

        if new_pos == self.apple:
            self.lenght += 1
            self.score += 1
            if self.score >= self.high_score:
                self.high_score = self.score
            self.apple = self.new_apple_location

        self.head = new_pos

    def test_move_up_1_times(self):
        self.head = [5, 5]
        self.lenght = 3
        self.direction = UP
        self.do_move()

        self.assertEqual(self.head, [5, 6])


    def test_move_down_3_times(self):
        self.head = [5, 5]
        self.lenght = 3
        self.direction = DOWN
        self.do_move()
        self.do_move()
        self.do_move()

        self.assertEqual(self.head, [5, 2])
