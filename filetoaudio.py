from gtts import gTTS
import os
text=open('dem.txt','r' ,encoding= 'utf-8').read()
language='hi'
output=gTTS(text=text,lang=language,slow=False)
output.save('a.mp3')
os.system('start a.mp3')
