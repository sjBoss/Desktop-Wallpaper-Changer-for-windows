import tkinter as tk
from tkinter import Tk
import os
import tkinter.filedialog

root = Tk()
root.geometry("300x245")
root.resizable(width = False,height = False)

file_opt = options = {}
options['filetypes'] = [('all files', '.*')]
options['initialdir'] = 'C:\\'
options['parent'] = root
options['title'] = 'Browse'

import subprocess

filepath="C:\\dist\\Install\\filename.bat"
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

stdout, stderr = p.communicate()

def but_def():
   file1 = open("C:\\dist\\location.txt","w")
   file1.write(location.get())
   file1.close()
   root.quit()

def openFileName(event):
   global filename
   filename = tk.filedialog.askdirectory()
   location.insert(0,filename)
   print(filename)

label1 = tk.Label(text = "  Welcome to \nWallpaperChanger",font = " ComicSansMS 17 bold ",foreground = "red")
label1.place(relx = 0.5,rely = 0.13,anchor = "center")

label2 = tk.Label(text = "  Set image location",font = "Arial 12",foreground = "black")
label2.place(relx = 0.485,rely = 0.37,anchor = "center")

location = tk.Entry(text = "Enter",width = 32,relief = tk.GROOVE,bd = 4,font = "Arial 10 bold",foreground = "black")
location.place(relx = 0.5,rely = 0.5, anchor = "center")

browse = tk.Button(text = "::",relief = tk.GROOVE,overrelief = tk.GROOVE,fg = "cyan")
browse.place(relx = 0.92,rely = 0.5, anchor = "center")
browse.bind("<Button-1>",openFileName)

button = tk.Button(text = " Install ",relief = tk.GROOVE,overrelief = tk.GROOVE,font = "Arial 11 bold",command = but_def)
button.place(relx = 0.5, rely = 0.7,anchor = "center")

blue = tk.PhotoImage(file = "C:\\dist\\download.png")

label2 = tk.Label(image = blue)
label2.place(relx = 0.5,rely = 1.2,anchor = "center")

label1 = tk.Label(text = "SJ Technologies",font = " ComicSansMS 13 bold ",foreground = "orange",background = "blue4")
label1.place(relx = 0.5,rely = 0.93,anchor = "center")

root.mainloop()
