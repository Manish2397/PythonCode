import speech_recognition as sr
from commands.commands import getcommands

r=sr.Recognizer()
print(sr.Microphone.list_microphone_names())


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold = 600

    cnt=0
    text=""
    while True:
        cnt+=1
        if(cnt%10==0):
            print("say anything : ",cnt)
            audio = r.record(source, duration=5)
            with open("audio.wav", "wb") as f:
                f.write(audio.get_wav_data())
            try:
                recordedtext = r.recognize_google(audio)
                print(recordedtext)
                if(recordedtext.split(" ")[0]=="command"):
                    getcommands(recordedtext,text)
                else:
                    text+=" "
                    text+=recordedtext
            except:
                print("sorry, could not recognise")


