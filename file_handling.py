with open("sample_audio.mp3","rb") as my_file:
    content=my_file.read()


with open("audio_copy.mp3","wb") as my_file:
    my_file.write(content)
