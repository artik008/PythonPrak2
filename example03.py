#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''

from tkinter import *
import random


def getColor(i):
  ii = 1
  f = open('colors', 'r')
  for line in f:
    if ii == i:
      spl = line.split()
      if len(spl) == 5:
        i+=1
        ii+=1
      else:
        return line.split()[3]
        f.close()
        break
    else:
      ii+=1

TKroot = Tk()
TKroot.title("Prak")
TKroot.geometry('600x100+200+100')

root = Frame(TKroot)
root.place(relx=0, rely=0, relheight=1, relwidth=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# root.pack( side = BOTTOM )

Txt = Label(root, text="Colored Label", bg="PeachPuff")

def setColors(event):
  c1 = random.randint(1, 752)
  c2 = random.randint(1, 752)
  print(c1,c2)
  t1 = getColor(c1)
  t2 = getColor(c2)
  print(t1)
  print(t2)
  Txt.configure(bg = t1, fg = t2)



Exit = Button(root, text="Quit!", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W)

Butt = Button(root, text="Add")

def change(event):
  print("change")

def add(event):
  Butt.configure(text="Change")
  Butt.bind('<Button-1>', setColors)
  Txt.grid(row=0, column=1, sticky=E+W+S+N)
  Exit.grid(row=0, column=2, sticky=E+W)
  Butt.grid(row=0, column=0, sticky=E+W+S+N)
  root.columnconfigure(2, weight=1)

Butt.bind('<Button-1>', add)
Butt.grid(row=0, column=0, sticky=E+W)


TKroot.mainloop()
print("Done")
#root.destroy()
