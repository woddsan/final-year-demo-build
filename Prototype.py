#imports
from binascii import rlecode_hqx
from email import message
from email.mime import audio
from fileinput import filename
from turtle import done
from unittest import skip
from neuralintents import GenericAssistant
from pyparsing import null_debug_action
import speech_recognition as sr
import pyttsx3 as tts
import sys
import pywhatkit
import webbrowser
from gtts import gTTS
import playsound
import re
import random
#login and add user
name = str(input("What's your name? \n"))
if name == "":
    while name=="":
        name = str(input("The one with no name?Surely you must have one \n"))


def texttoSpeech(text):
    my_audio=gTTS(text)
    my_audio.save("output.mp3")
    playsound.playsound("output.mp3")

texttoSpeech("Hello"+name)

#username check and add
names = [line.strip() for line in open("username.txt")]


if name in names:
    print("Yes")
else:
    f=open(name+".txt","w+")
    f.close
    p=open("username.txt","a")
    p.write(name+ "\n")
    p.close


texttoSpeech("How many hours is your average work session?")
timeslot = input("How many hours is your average work session? \n")

texttoSpeech("Please Enter")
water = input("Please enter water intake goal (Liters). A good starting point can be 4 liters. \n")
#interval = input("You can add time interval.")

recognizer = sr.Recognizer()
r=sr.Recognizer()


"""
def addContact():
    #enter name
    #enter contact




def hello():
    greet = ["Hi", "Hello","Hello There","What is up","Hiya","Hey","Hello and Welcome"]
    sel=random.randint(0,7)
    texttoSpeech(greet[sel])

def playMusic():
    None

def sendMessage():
    None

def sendEmail():
    webbrowser.open("https://mail.google.com/mail/u/2/#inbox?compose=new")

def waterRemind():
    None

def searchGoogle():
    None

def addContact(name):
    None

def quit():
    
    sys.exit(0)
"""
