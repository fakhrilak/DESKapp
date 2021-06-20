from tkinter import *

# class Table:
#     def __init__(self,root,total_columns,data,query):
#         result = []
#         for a in range(len(data)):
#             result.append((data[a],query[a]))
#         print(result[0])
#         for i in range(len(result)):
#             for j in range(total_columns):
                  
#                 self.e = Entry(root, width=60, fg='blue',
#                                font=('Arial',10,'bold'))
                  
#                 self.e.grid(row=i, column=j)
#                 self.e.insert(END, result[i][j])


class Table:
    def __init__(self,canvas,data,x,y,w):
        for i in range(len(data)):
            label = Entry(font=('helvetica', 10, 'bold'),bg='white',width=w)
            label.insert(END,data[i])
            canvas.create_window(x,y+(20*i),window=label)
