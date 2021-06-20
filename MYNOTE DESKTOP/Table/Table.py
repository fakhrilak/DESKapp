from tkinter import *
class Table:
    def __init__(self,canvas,data,x,y,w):
        for i in range(len(data)):
            label = Entry(font=('helvetica', 10, 'bold'),bg='white',width=w)
            label.insert(END,data[i])
            canvas.create_window(x,y+(20*i),window=label)