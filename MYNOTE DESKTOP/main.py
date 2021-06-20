from tkinter import *
from config import config
from Table import Table

root = Tk()
root.title("MY-note")

command = Entry(root)

data = config.getAll_data("users")

Table.Table(root,data)

root.mainloop()