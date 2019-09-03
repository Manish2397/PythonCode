import speech_recognition as sr
import pyperclip
import os
r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold = 600
    print("say anything : ")
    audio= r.record(source,duration=2)
    with open("audio.wav","wb") as f:
        f.write(audio.get_wav_data())
    try:
        text = r.recognize_google(audio)
        pyperclip.copy(text)
        print(text)
        pyperclip.copy(text)
        print(pyperclip.paste(text))


    except:
        print("sorry, could not recognise")
