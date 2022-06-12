from ctypes import resize
import tkinter as tk
from tkinter import Text,ttk
import os
from tkinter import *

cwd = os.getcwd()

root = tk.Tk()

root.geometry("810x400")
root.title('Agent instalock')
root.resizable(0, 0)

bg = PhotoImage(file = cwd + "\Valorant_instalock\img.png")

pic = Label( root, image = bg)
pic.place(x = 0, y = 100)

def tabelFor():   
   boxH = 37
   boxW = 37

   for r in range(3):
      for c in range(9):
         num = ""
         if r == 0:
            num = num
         elif r == 1:
            num = c+1
         elif r == 2:
            num = c+10

         tabelLabel = ttk.Button(root, text=num)
         tabelLabel.grid(column=c, row=r, sticky=tk.W, padx=boxW, pady=boxH)

tabelFor()

if __name__ == "__main__":
   root.mainloop()

