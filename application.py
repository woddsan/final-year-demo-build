import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, QtMsgType
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from frontend import Ui_MainWindow
import requests
from binascii import rlecode_hqx
from cgitb import text
from email import message
from email.mime import audio
from fileinput import filename
import os
from time import sleep
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
import pyjokes
import wikipedia
from socket import timeout
import time
import schedule
import subprocess

from matplotlib.pyplot import title
from plyer import notification
import random
import importlib




songlist = ["Toy Story you got a friend in me","Rick Astley Never Gonna Give you Up","Shrek somebody once told me","pharrell happy","liam payne sunshine"]

totalstepcount=0


def stepNotif():
    notification.notify(
        title = "You can walk a few steps",
        message = "Activity Time",
        #app_icon = "Iconsmind-Outline-Wine-Bottle.ico",
        timeout=2
        )
    

def check():
    import testemodet
    
    mood = testemodet.emodet()
    
    

    if mood == "Neutral" :
        print("Neutral")
        texttoSpeech("Going good. Let's Keep it up")
        
        
    elif mood == "Happy":
        print("happy")
        texttoSpeech("We like a smiley face. Let's go")
        
        
    elif mood == "Sad":
        print("Sad")
        texttoSpeech("I can cheer you up with this song")
        sel=random.choice(range(0,len(songlist)))
        playMusic(songlist[sel])
        

    elif mood == "Angry":
        print("ANGRY")
        texttoSpeech("let's kick back and relax a little")
        notif()
        

    elif mood=="":
        print("none")
    
    elif mood=="No faces found":
        texttoSpeech("No face found please sit properly")
        


#notif
def notif():
        notification.notify(
        title = "Have some water",
        message = "Keep yourself  Hydrated",
        #app_icon = "Iconsmind-Outline-Wine-Bottle.ico",
        timeout=5
        )

def notif():
        notification.notify(
        title = "Have some water",
        message = "Keep yourself  Hydrated",
        #app_icon = "Iconsmind-Outline-Wine-Bottle.ico",
        timeout=5
        )


#textToSpeech
def texttoSpeech(text):
    my_audio=gTTS(text)
    my_audio.save("noutput.mp3")
    playsound.playsound("noutput.mp3")
    sleep(1)
    os.remove("noutput.mp3")


#query


def tellJoke():
    punchline=pyjokes.get_joke()
    texttoSpeech(punchline)

def searchGoogle(url_build):
    linereq=str(url_build.split(' ',1)[1:])
    webbrowser.open("https://www.google.com/search?q="+linereq)

def sumWiki(wikuery):
    wikreq=str(wikuery.split(' ',1)[1:])
    try:
        summary=wikipedia.summary(wikreq,sentences=1)
        texttoSpeech(summary)
    except Exception as x:
        webbrowser.open("https://en.wikipedia.org/wiki/"+wikreq)



def hello():
    greet = ["Hi", "Hello","Hello There","What is up","Hiya","Hey","Hello and Welcome"]
    sel=random.randint(0,6)
    texttoSpeech(greet[sel])
    texttoSpeech("I will scan your face now. Please stand infront of the camera.")
    

def playMusic(trackName):
    tracks=str(trackName.split(' ',1)[1:])
    texttoSpeech("playing"+tracks)
    sleep(2)
    pywhatkit.playonyt(tracks)

def sendEmail():
    webbrowser.open("https://mail.google.com/mail/u/2/#inbox?compose=new")


def quit():
    
    sys.exit(0)



class MainThread(QThread):
    

    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):

        #hello()
        notif()
        hello()
        check()
        self.schdFun()




    def commandInput(self):
        recognizer = sr.Recognizer()
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source,duration=1)
            audio = r.listen(source)
        try:
            print("Recognizing..")
            qry=r.recognize_google(audio,language="en-in")
            run=str(qry)
            run=run.lower()
                
        except Exception as e:
            return "none"
        return run

    def queryExecute(self):
        
        self.query = self.commandInput()

        command=self.query.split(' ',1)[0]
        if command=="hello":
            hello()
        if command=="play":
            playMusic(self.query)
        if command=="exit" or command=="quit" or command =="bye":
            quit()
        if command=="send" or command=="email" or command=="mail":
            sendEmail()
        if command=="search":
            searchGoogle(self.query)
        if command =="joke" or command=="tell":
            tellJoke()
        if command =="summarize" or command =="summary" or command=="summarise":
            sumWiki(self.query)
            
        else:
            pass
    
    def schdFun(self):
        startTime=int(time.time())
        

        while True:
            newTime=int(time.time())
            newCount=newTime-startTime
            if newCount>=300:
                notif()
                check()
                startTime=int(time.time())
                
            
            else:
                self.queryExecute()

    


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask) 
        self.ui.pushButton_3.clicked.connect(self.steps)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        
        self.ui.movie =  QtGui.QMovie("tumblr_nfetk2UwcB1sj5h4oo1_1280.webp")  
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        
        

    def showTime(self):
        current_time=QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

    def steps(self):
        url = "https://v1.nocodeapi.com/zetaknight/fit/GpWLJGwidrAOkBVc/aggregatesDatasets?dataTypeName=steps_count,active_minutes,calories_expended&timePeriod=today"
        params = {}
        r = requests.get(url = url, params = params)
        result = r.json()
        steps=str(result['steps_count'][0]['value'])
        active=str(result['active_minutes'][0]['value'])
        calories=str(result['calories_expended'][0]['value'])
        self.ui.textBrowser_3.setText(steps)
        self.ui.textBrowser_7.setText(active)
        self.ui.textBrowser_8.setText(calories)

        try:
            
            st=str(result['steps_count'][0]['value'])
            self.ui.textBrowser_3.setText(st)
        
        except:
            texttoSpeech("Your smart device is not connected")

        
        """
        if totalstepcount==0:
            totalstepcount=ncount
        elif ncount<totalstepcount:
            stepNotif()
        """



app = QApplication(sys.argv)
baymax = Main()
baymax.show()
exit(app.exec_())