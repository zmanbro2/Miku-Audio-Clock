
from datetime import datetime
import playsound
from time import sleep
import pystray
import PIL.Image
import threading
import os





Image = PIL.Image.open("Miku.ico")

def gettime():
   global now,Hour,Minute,minutetillhour
   now = datetime.now()
   Hour = now.strftime("%H")
   Minute = now.strftime("%M")
   minutetillhour = 60 - int(Minute)  

gettime()


def Clock(): 
   seccondtillhour = minutetillhour * 60
   print("offset:","|min|",Minute,"|MinTil|",minutetillhour,"|SecTil|",seccondtillhour)
   print("Clock Starting!")
   playsound.playsound('Miku/' + Hour + '.mp3')
   print("Sound Played!",Hour,Minute)
   sleep(seccondtillhour)
   gettime()
   print("Restarting!")
   Clock()
  
  
def startClock(): 
 t = threading.Thread(target=Clock)
 t.start()
 



    
def on_clicked(icon, item): 
    os._exit(0)

icon = pystray.Icon("Miku", Image, menu=pystray.Menu(
    pystray.MenuItem("Stop Clock", on_clicked),
))

startClock()
icon.run()
   






 














