from tkinter import Tk, Label


def key_pressed(event):
 print('no')


root=Tk()
root.bind("<Key>",key_pressed)
root.mainloop()