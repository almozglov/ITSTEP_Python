
from tkinter import filedialog as fd, messagebox as mb, colorchooser
from PIL import Image, ImageTk, ImageGrab

def save_my_paint():
    global w
    lpx = w.winfo_rootx()
    lpy = w.winfo_rooty()
    rpx = lpx + w.winfo_width()
    rpy = lpy + w.winfo_height()
    filename = fd.asksaveasfilename()
    ImageGrab.grab([lpx, lpy, rpx, rpy]).save(filename)

filemenu.add_command(label="Сохранить...", command=save_my_paint)
