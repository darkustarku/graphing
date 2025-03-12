from tkinter import *
from tkinter import ttk

root = Tk()
root.title("pyGraph")

MainFrame = ttk.Frame(root, relief="ridge", width=600, height=700)

canvas = Canvas(MainFrame, width=500, height=400, background="gray75")


MainFrame.grid()
canvas.grid(column=2, row=2)

canvas.create_oval(100, 100, 200, 200, fill="blue", outline="black")
graph_options = Listbox(canvas, height=3)

for child in MainFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)




root.mainloop()

