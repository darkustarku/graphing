from tkinter import *
from tkinter import ttk

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

CANVAS_WIDTH = WINDOW_WIDTH - 200
CANVAS_HEIGHT = WINDOW_HEIGHT - 100 

def drawNode(canvas, node, radius):
    canvas.create_oval(node.x, node.y, node.x + radius, node.y + radius, fill="blue", outline="black")
    return 


def createWindow(root, userWidth, userHeight, circles):
    root.title("pyGraph")

    Window = ttk.Frame(root, relief="ridge", width=userWidth, height=userHeight)
    canvas = Canvas(Window, width=(userWidth-200), height=(userHeight - 100), background="gray75")

    Window.grid()
    canvas.grid(column=2, row=2)

    circle_radius = 0.1 * userHeight


    for child in Window.winfo_children():
        child.grid_configure(padx=5, pady=5)

    return root










