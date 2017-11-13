##  IMPORTING MODULES ##
from picamera import PiCamera
from time import sleep

## MAIN CODE ##

#Variables
camera = PiCamera() 
PhotoNumber = 1 #this is a variable to store the n.o of the photo that has been taken
#Body of code
for i in range(5): # repeats the loop 5 times
    camera.start_preview()#starts camera preview
    sleep(5)#waits for 5 seconds
    camera.capture('/home/pi/AstroPi/CloudCover'+PhotoNumber)#takes a photo and calls it CloudCover then a number
    camera.capture('/home/pi/AstroPi/ColourIndex'+PhotoNumber)#takes a photo and calls it colourIndex then a number
    camera.stop_preview()#stops the preview
    PhotoNumber = PhotoNumber+1 #adds one to the variable photo nmber
    sleep(55)#waits for 55 seconds
               

