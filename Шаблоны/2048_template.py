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
    # Получаем координаты ячейки матрицы
    # и добавляем туда двойку
    a = random.randint(0, GRID_LEN-1)
    b = random.randint(0, GRID_LEN-1)
    # Проверяем, что ячейка матрицы пустая
    while matrix[a][b] != 0:
        # Выбираем новые координаты до тех пор,
        # пока не найдём пустую ячейку
        a = random.randint(0, GRID_LEN-1)
        b = random.randint(0, GRID_LEN-1)
    matrix[a][b] = 2


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
    done = False
    for i in range(len(mat)):
        for j in range(len(mat)-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return (mat, done)


def move_up():
    pass


def move_down():
    pass


def move_left():
    # ШАПИТО. Трогать осторожно
    global matrix
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    return done




def move_right():
    pass


def init_grid():
    # Создаём окошко игры (указываем ему цвет и размеры)
    background = Frame(
        bg=BACKGROUND_COLOR_GAME,
        width=SIZE,
        height=SIZE
    )
    background.grid()
    for i in range(GRID_LEN):
        grid_row = []
        for x in range(GRID_LEN):
            cell = Frame(background,
                         bg=BACKGROUND_COLOR_CELL_EMPTY,
                         width=SIZE/GRID_LEN,
                         height=SIZE/GRID_LEN)
            cell.grid(row=i, column=x,
                      padx=GRID_PADDING, pady=GRID_PADDING)
            cell_text = Label(
                master=cell, text='', justify=CENTER,
                font=FONT, width=5,height=2)
            cell_text.grid()
            grid_row.append(cell_text)
        grid_cells.append(grid_row)


def init_matrix():
    for i in range(GRID_LEN):
        matrix.append([0]*GRID_LEN)
    # Добавляем две двойки в матрицу
    add_two()
    add_two()

def update_grid_cells():
    for a in range(GRID_LEN):
        for b in range(GRID_LEN):
            if matrix[a][b] == 0:
                grid_cells[a][b].config(
                    text='',
                    bg=BACKGROUND_COLOR_CELL_EMPTY)
            else:
                grid_cells[a][b].config(
                    text=matrix[a][b],
                    bg=BACKGROUND_COLOR_DICT[matrix[a][b]],
                    fg=CELL_COLOR_DICT[matrix[a][b]])



def key_pressed(event):
    pass


init_grid()
init_matrix()
update_grid_cells()

mainframe.master.title('MYSUPERDUPERPUPER2048')
# БИНДИМ НАЖАТИЯ КНОПОК К ДЕЙСТВИЯМ
mainframe.master.bind("<Key>", key_down)

mainframe.commands = {KEY_UP: up, KEY_DOWN: down,
KEY_LEFT: left, KEY_RIGHT: right}



mainloop()
