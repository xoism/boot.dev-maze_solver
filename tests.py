
import unittest

from maze import Maze
from window import Point


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = [12, 14, 16, 1]
        num_rows = [10, 8, 6, 100]
        for r in num_rows:
            for c in num_cols:
                m1 = Maze(Point(0,0), r, c, 10)
                self.assertEqual(len(m1._cells), r, 'unexpected row count')
                self.assertEqual(len(m1._cells[0]), c, 'unexpected column count')


if __name__ == '__main__':
    unittest.main()
