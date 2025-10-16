from gtts import gTTS

import  os

s=gTTS(text="Hello",slow=False,lang='en')
print(type(s))

s.save("sample_audio.mp3")

# os.system("start sample_audio.mp3")