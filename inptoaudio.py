from gtts import gTTS
import os
from tkinter import *
root=Tk()
canvas= Canvas(root,width=400,height=300)
canvas.pack()
def texttospeech():
    text =entry.get()
    output = gTTS(text=text, lang='en', slow=False)
    output.save('out.mp3')
    os.system('start out.mp3')

entry=Entry(root)
canvas.create_window(200,180,window=entry)
button =Button(text="start",command=texttospeech)
button.pack()
canvas.create_window(200,230,window=entry)

root.mainloop()
