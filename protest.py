import testemodet
import schedule
import time
import datetime
from importlib import reload
reload(testemodet)


def looper(an):
    for k in range(0,10):
        print(an)
        time.sleep(1)


def check():
    time.sleep(5)
    mood = testemodet.emodet()
    

    if mood == "Neutral" :
        looper("N")
        
    elif mood == "Happy":
        looper("H")
        
    elif mood == "Sad":
        looper("tell joke")

    elif mood == "Angry":
        looper("calm down")

    elif mood=="":
        looper("kya")

def rec():
    for i in range (0,20):
        print ("not print \n")
    time.sleep(1)


if __name__=="__main__":
    check()

    
    
    
        



        
        

        
        

    
