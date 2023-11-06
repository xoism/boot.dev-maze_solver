
import random
from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color:str):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        canvas.pack()


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title = 'boot.dev maze solver'
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
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
    
    def draw_line(self, line: Line, fill_color:str):
        line.draw(self.canvas, fill_color)


def main():
    win = Window(800, 600)
    for _ in range(5):
        p1 = Point(random.randrange(800), random.randrange(600))
        p2 = Point(random.randrange(800), random.randrange(600))
        line = Line(p1, p2)
        win.draw_line(line, random.choice(['red', 'black', 'yellow', 'green', 'blue', 'black', 'orange', 'chartreuse', 'purple', 'brown']))
    win.wait_for_close()


if __name__ == '__main__':
    main()
