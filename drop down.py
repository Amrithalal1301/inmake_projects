from tkinter import *
from tkinter import messagebox
root =Tk()
def fun1():
   messagebox.askyesno(title="Do you want to exit?")

note = Menu(root)
root.config(menu=note)

note1=Menu(note)

note.add_cascade(label="file",menu=note1)
note1.add_command(label="new project")
note1.add_command(label="open project")
note1.add_separator()
note1.add_command(label="Save As")
note1.add_command(label="Save..")
note1.add_separator()
note1.add_command(label="exit",command=fun1)

note2=Menu(note)

note.add_cascade(label="Edit",menu=note2)
note2.add_command(label="Undo")
note2.add_command(label="Redo")
note2.add_separator()
note2.add_command(label="Cut")
note2.add_command(label="Copy")
note2.add_separator()
note2.add_command(label="Recent files")


root.mainloop()
