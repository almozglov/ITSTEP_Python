import random
from tkinter import *

SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = "#92877d"
BACKGROUND_COLOR_CELL_EMPTY = "#9e948a"

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                         16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                         1024: "#edc53f", 2048: "#edc22e"}

CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
                   32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
                   256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",
                   2048: "#f9f6f2"}

FONT = ("Verdana", 40, "bold")

KEY_UP = "'w'"
KEY_DOWN = "'s'"
KEY_LEFT = "'a'"
KEY_RIGHT = "'d'"


mainframe = Frame()
grid_cells = []
matrix = []


def add_two():
    pass


def check_game_state():
    pass


def reverse(mat):
    pass


def transpose(mat):
    pass

def cover_up(mat):
    # Двигать все ячейки матрицы влево (но не
    # сливает их)
    new = []
    for i in range(len(mat)):
        new.append([0] * len(mat))
    done = False
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat)):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
            count += 1
    return (new, done)


def merge(mat):
    pass


def move_up():
    pass


def move_down():
    pass


def move_left():
    pass


def move_right():
    pass


def init_grid():
    pass


def init_matrix():
    pass


def update_grid_cells():
    pass

def key_pressed(event):
    pass
