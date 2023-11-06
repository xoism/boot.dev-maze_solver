
from __future__ import annotations

from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __call__(self) -> (int, int):
        return self.x, self.y

    def __add__(self, other:(int, int)) -> Point:
        x, y = other
        return Point(self.x + x, self.y + y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color:str = 'black'):
        canvas.create_line(self.p1(), self.p2(), fill=fill_color, width=2)
        canvas.pack()

    def __str__(self) -> str:
        return f"Line({self.p1}, {self.p2})"


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title = 'boot.dev maze solver'
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.window_is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()

    def close(self):
        self.window_is_running = False
    
    def draw_line(self, line: Line, fill_color:str = 'black'):
        line.draw(self.canvas, fill_color)

    @property
    def bg(self):
        return self.canvas.cget('bg')
