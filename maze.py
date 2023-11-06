
from time import sleep

from cell import Cell
from window import Point, Window


class Maze:
    def __init__(self, top_left: Point, rows:int, columns: int, cell_size: int, win: Window = None):
        self._top_left = top_left
        self._rows = rows
        self._columns = columns
        self._cell_size = cell_size
        self._win = win
        self._cells:[[Cell]] = []

        self._create_cells()
        self._break_entrance_and_exit()
    
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
        sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(-1, -1)
