
import random

from itertools import product

from tkinter import Tk, BOTH, Canvas

from colors import COLORS


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __call__(self) -> (int, int):
        return self.x, self.y

class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color:str = 'black'):
        canvas.create_line(self.p1(), self.p2(), fill=fill_color, width=2)
        canvas.pack()


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


class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, window: Window):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self._top_left = top_left
        self._bottom_right = bottom_right
        self._top_right = Point(bottom_right.x, top_left.y)
        self._bottom_left = Point(top_left.x, bottom_right.y)
        self._win = window
    
    def draw(self, color:str = 'black'):
        if self.left_wall:
            self._win.draw_line(Line(self._top_left, self._bottom_left), fill_color=color)
        if self.right_wall:
            self._win.draw_line(Line(self._top_right, self._bottom_right), fill_color=color)
        if self.top_wall:
            self._win.draw_line(Line(self._top_left, self._top_right), fill_color=color)
        if self.bottom_wall:
            self._win.draw_line(Line(self._bottom_left, self._bottom_right), fill_color=color)
        

# https://chat.openai.com/share/df37ea1c-988d-4be3-b754-e6d8bc62e1ce
# https://stackoverflow.com/questions/27757973/generating-all-possibly-length-n-combinations-of-two-items-in-python
def generate_boolean_combinations():
    for combination in product([True, False], repeat=4):
        yield combination


def main():
    win = Window(800, 600)
    for _ in range(5):
        p1 = Point(random.randrange(800), random.randrange(600))
        p2 = Point(random.randrange(800), random.randrange(600))
        line = Line(p1, p2)
        win.draw_line(line, random.choice(COLORS))
    for combo in generate_boolean_combinations():
        p1 = Point(random.randrange(800-30), random.randrange(600-30))
        p2 = Point(p1.x + 30, p1.y + 30)
        cell = Cell(p1, p2, win)
        cell.left_wall, cell.right_wall, cell.top_wall, cell.bottom_wall = combo
        cell.draw(random.choice(COLORS))

    win.wait_for_close()


if __name__ == '__main__':
    main()
