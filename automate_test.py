from fileinput import close
from time import sleep
from pywinauto.application import Application
app = Application(backend="uia")
app.start(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

sleep(5)
app.minimize()