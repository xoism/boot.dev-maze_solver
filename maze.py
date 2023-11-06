
import itertools
import random
from time import sleep

from cell import Cell
from window import Point, Window


class Maze:
    def __init__(self, top_left: Point, rows:int, columns: int, cell_size: int, win: Window = None, seed: int = None, anim_delay: float = 0.01):
        if seed is not None:
            random.seed(seed)

        self.anim_delay = anim_delay

        self._top_left = top_left
        self._rows = rows
        self._columns = columns
        self._cell_size = cell_size
        self._win = win
        self._cells:[[Cell]] = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0, 0)
        self._reset_visited()
        print('maze ready')

    def _create_cells(self):
        for x in range(self._rows):
            row = []
            self._cells.append(row)
            top_left = self._top_left
            top_left += (0, x * self._cell_size)
            for y in range(self._columns):
                bottom_right = top_left + (self._cell_size, self._cell_size)
                cell = Cell(top_left, bottom_right, self._win)
                row.append(cell)
                self._draw_cell(x, y)
                top_left += (self._cell_size, 0)

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(self.anim_delay)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(-1, -1)

    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbors = [
                (x, y, d)
                for x, y, d in filter(
                    lambda x: 0 <= x[0] < self._rows and 0 <= x[1] < self._columns,
                    [(i-1, j, 'u'), (i+1, j, 'd'), (i, j-1, 'l'), (i, j+1, 'r')]
                )
                if not self._cells[x][y].visited
            ]

            if len(neighbors) == 0:
                self._draw_cell(i, j)
                return

            x, y, d = random.choice(neighbors)
            match d:
                case 'l':
                    self._cells[i][j].left_wall = False
                    self._cells[x][y].right_wall = False
                case 'r':
                    self._cells[i][j].right_wall = False
                    self._cells[x][y].left_wall = False
                case 'u':
                    self._cells[i][j].top_wall = False
                    self._cells[x][y].bottom_wall = False
                case 'd':
                    self._cells[i][j].bottom_wall = False
                    self._cells[x][y].top_wall = False

            self._break_walls(x, y)

    def _reset_visited(self):
        for cell in itertools.chain.from_iterable(self._cells):
            cell.visited = False
