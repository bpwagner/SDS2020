from tkinter import *

#https://pypi.org/project/tkmacosx/
#pip3 install tkmacosx
from tkmacosx import Button

def Color(c):
  print(c)
  pass

def Delete():
    pass

def Check():
    pass

root = Tk()
root.title("MasterMind")
root.configure(background = 'white')

frame1 = Frame(root, bg='sky blue', bd= 10)
frame1.pack(side=TOP)

canvas1 = Canvas(frame1, width = 400, height=400)
canvas1.pack()

frame2 = Frame(root)

c1 = Button(frame2, text=" ", borderless=1, bg='magenta2', command=lambda: Color('R'))
c1.pack(side=LEFT)

c2 = Button(frame2, text=" ", borderless=1, bg='cyan', command=lambda: Color('C'))
c2.pack(side=LEFT)

c3 = Button(frame2, text=" ", borderless=1, bg='purple2', command=lambda: Color('P'))
c3.pack(side=LEFT)

c4 = Button(frame2, text=" ", borderless=1, bg='teal', command=lambda: Color('T'))
c4.pack(side=LEFT)

c5 = Button(frame2, text=" ", borderless=1, bg='yellow', command=lambda: Color('Y'))
c5.pack(side=LEFT)

c6 = Button(frame2, text=" ", borderless=1, bg='dark green', command=lambda: Color('D'))
c6.pack(side=LEFT)

b1 = Button(frame2, text="Delete", command=Delete)
b1.pack(side=RIGHT)

b2 = Button(frame2, text="Check", command=Check)
b2.pack(side=RIGHT)


frame2.pack(side=BOTTOM)

mainloop()