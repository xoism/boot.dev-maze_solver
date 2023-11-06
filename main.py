

import random
from itertools import product


from cell import Cell
from colors import COLORS
from maze import Maze
from window import Line, Point, Window


# https://chat.openai.com/share/df37ea1c-988d-4be3-b754-e6d8bc62e1ce
# https://stackoverflow.com/questions/27757973/generating-all-possibly-length-n-combinations-of-two-items-in-python
def generate_boolean_combinations():
    for combination in product([True, False], repeat=4):
        yield combination


def center_maze(rows:int, columns: int, cell_size: int, win_width: int, win_height: int) -> Point:
    width = columns * cell_size
    height = rows * cell_size
    x = (win_width // 2) - (width // 2)
    y = (win_height // 2) - (height // 2)
    return Point(x, y)


def main():
    win = Window(800, 600)
    ## test drawing lines
    # for _ in range(5):
    #     p1 = Point(random.randrange(800), random.randrange(600))
    #     p2 = Point(random.randrange(800), random.randrange(600))
    #     line = Line(p1, p2)
    #     win.draw_line(line, random.choice(COLORS))
 
    ## test drawing cells
    # previous_cell = None
    # for combo in generate_boolean_combinations():
    #     p1 = Point(random.randrange(800-30), random.randrange(600-30))
    #     p2 = Point(p1.x + 30, p1.y + 30)
    #     cell = Cell(p1, p2, win)
    #     cell.left_wall, cell.right_wall, cell.top_wall, cell.bottom_wall = combo
    #     cell.draw(random.choice(COLORS))
    #     if previous_cell:
    #         cell.draw_move(previous_cell, random.choice([True, False]))
    #     previous_cell = cell

    ## test drawing maze
    rows, columns, size = 17, 13, 30
    maze_loc = center_maze(rows, columns, size, 800, 600)
    # win.draw_line(Line(Point(400,300), Point(430, 330)), 'red')
    maze = Maze(maze_loc, rows, columns, size, win, 2)

    win.wait_for_close()


if __name__ == '__main__':
    main()
