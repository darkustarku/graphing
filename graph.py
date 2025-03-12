from tkinter import *
from tkinter import ttk 
import display as dp
import nodes as nd

root = Tk()
nodes = {}



window = dp.createWindow(root, 1200, 800, nodes)


window.mainloop()