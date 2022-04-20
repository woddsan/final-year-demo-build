from tkinter import N
import speech_recognition as sr
import pyttsx3 as tts
import sys



recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 120)


speaker.say("Hello World")
speaker.runAndWait()


r=sr.Recognizer()
with sr.Microphone() as source:
    print("Listening")
    r.pause_threshold=1
    r.adjust_for_ambient_noise(source,duration=0.2)
    audio = r.listen(source)

try:
    print("Recognizing..")
    query=r.recognize_google(audio,language="en-in")
    speaker.say(f"User said:{query}\n")
    speaker.runAndWait()

except Exception as e:
    print(e)

    speaker.say("come again")
    speaker.runAndWait()