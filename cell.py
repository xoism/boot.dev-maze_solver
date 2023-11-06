
from __future__ import annotations

from window import Line, Point, Window

class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, window: Window = None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._top_right = Point(bottom_right.x, top_left.y)
        self._bottom_left = Point(top_left.x, bottom_right.y)
        self._center = Point(
            (top_left.x + bottom_right.x) // 2,
            (top_left.y + bottom_right.y) // 2
        )
        self._win = window
    
    @property
    def center(self) -> Point:
        return self._center

    def draw(self, color:str = 'black'):
        if self._win is None:
            return
        self._win.draw_line(Line(self._top_left, self._bottom_left), fill_color=color if self.left_wall else self._win.bg)
        self._win.draw_line(Line(self._top_right, self._bottom_right), fill_color=color if self.right_wall else self._win.bg)
        self._win.draw_line(Line(self._top_left, self._top_right), fill_color=color if self.top_wall else self._win.bg)
        self._win.draw_line(Line(self._bottom_left, self._bottom_right), fill_color=color if self.bottom_wall else self._win.bg)

    def draw_move(self, to_cell: Cell, undo:bool = False):
        if self._win is None:
            return
        self._win.draw_line(Line(self.center, to_cell.center), 'red' if undo else 'gray')

    def __str__(self) -> str:
        return f"Cell({self._top_left}, {self._bottom_right})"

    def __repr__(self) -> str:
        return str(self)
