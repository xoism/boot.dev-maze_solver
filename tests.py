
import unittest

from maze import Maze
from window import Point


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = [12, 14, 16, 1]
        num_rows = [10, 8, 6, 100]
        for r in num_rows:
            for c in num_cols:
                maze = Maze(Point(0, 0), r, c, 10)
                self.assertEqual(len(maze._cells), r, 'unexpected row count')
                self.assertEqual(len(maze._cells[0]), c, 'unexpected column count')
    
    def test_maze_break_enter_exit(self):
        num_cols = 12
        num_rows = 10
        maze = Maze(Point(0, 0), num_rows, num_cols, 10)
        self.assertFalse(maze._cells[0][0].top_wall)
        self.assertFalse(maze._cells[9][11].bottom_wall)



if __name__ == '__main__':
    unittest.main(verbosity=2)
