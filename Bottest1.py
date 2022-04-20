#imports
from binascii import rlecode_hqx
from email import message
from email.mime import audio
from fileinput import filename
from turtle import done
from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import sys



recognizer = sr.Recognizer()
r=sr.Recognizer()


speaker = tts.init()
speaker.setProperty('rate', 120)

suggest_list=["Take some sips","Walk a few paces","Blink your eyes"]


def create_note():
    global r

    speaker.say("What do you want to write onto your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with sr.Microphone() as source:
                print("Listening")
                r.pause_threshold=1
                r.adjust_for_ambient_noise(source,duration=0.2)
                audio = r.listen(source)
                print("Recognizing..")
                note=r.recognize_google(audio,language="en-in")
                note=note.lower()

                speaker.say("Choose a filename!")
                speaker.runAndWait()

                r.adjust_for_ambient_noise(source,duration=0.2)
                audio=r.listen(source)

                filename=r.recognize_google(audio,language="en-in")
                filename=filename.lower()

            with open(filename,'w') as f :
                f.write(note)
                done=True
                speaker.say("Success")
                speaker.runAndWait()
        except sr.UnknownValueError:
            recognizer=sr.Recognizer()
            speaker.say("I did not understand")
            speaker.runAndWait()
                

   
def add_todo():
    global r

    speaker.say("What todo?")
    speaker.runAndWait()

    done= False

    while not done :
        try:
            with sr.Microphone() as source:
                r.pause_threshold=1
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio=r.listen(source)

                item = r.recognize_google(audio,language="en-in")
                item = item.lower()

                suggest_list.append(item)
                done = True

                speaker.say("Added to the list!")
                speaker.runAndWait()

        except sr.UnknownValueError:
            recognizer=sr.Recognizer()
            speaker.say("I did not understand. Please try again!")
            speaker.runAndWait()

def show_todos():

     speaker.say("the list has")
     for item in suggest_list:
         speaker.say(item)
         speaker.runAndWait()

def hello():
    speaker.say("Hello There")
    speaker.runAndWait()
    print ("hello success")

def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)

mappings = {
            "greeting":hello,
            "create_note":create_note,
            "add_todo":add_todo,
            "show_todos":show_todos,
            "exit":quit
}


assistant = GenericAssistant("intents.json",intent_methods=mappings)
assistant.train_model()

while True :
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language="en-in")
        run=str(query)
        
        run=run.lower()
        assistant.request(run)
        
    except Exception as e:
        print(e)

        speaker.say("come again")
        speaker.runAndWait()
    





        









