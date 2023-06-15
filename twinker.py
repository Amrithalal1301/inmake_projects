from tkinter import  *

root =Tk()
l1 =Label(root,text="Username")
l2 =Label(root,text="mobile")
l3 =Label(root,text="email")
l4 =Label(root,text="age")
l5 =Label(root,text="Pswd")
l6 =Label(root,text="New pswd")

entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4= Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)

# l1.pack()
# l2.pack()
# l3.pack()
# l4.pack()
# l5.pack()
# l6.pack()





l1.grid(row =0,column =0)
entry1.grid(row=0,column=1)
l2.grid(row =1,column =0)
entry2.grid(row=1,column=1)
l3.grid(row =2,column =0)
entry3.grid(row=2,column=1)
l4.grid(row =3,column =0)
entry4.grid(row=3,column=1)
l5.grid(row =4,column =0)
entry5.grid(row=4,column=1)
l6.grid(row =5,column =0)
entry6.grid(row=5,column=1)

frame1 =Frame(root)
# frame1.pack()
frame2 =Frame(root)
# frame2.pack()

but1 =Button(frame1,text="login",fg="white",bg="blue")
# but1.pack()
but2 =Button(frame2,text="Cancel",fg="white",bg="blue")
# but2.pack()

but2.grid(row=7,column=0)



root.mainloop()


