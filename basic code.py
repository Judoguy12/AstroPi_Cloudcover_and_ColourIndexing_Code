##  IMPORTING MODULES ##
from picamera import PiCamera
from time import sleep
from sense_hat import SenseHat

## MAIN CODE ##

#Variables
sense = SenseHat()
camera = PiCamera() 
PhotoNumber = 1 #this is a variable to store the n.o of the photo that has been taken
#Body of code
sense.show_message("Hello", text_colour = (0, 255, 0))
for i in range(2): # repeats the loop 5 times
    #camera.start_preview()#starts camera preview
    sleep(5)#waits for 5 seconds
    sense.show_message("Taking Picture", text_colour = (0, 0, 255))
    camera.capture('/home/pi/AstroPi/CloudCover(%d).jpeg' %PhotoNumber)#takes a photo and calls it CloudCover then a number
    camera.capture('/home/pi/AstroPi/ColourIndex(%d).jpeg' %PhotoNumber)#takes a photo and calls it colourIndex then a number
    #camera.stop_preview()#stops the preview
    PhotoNumber = PhotoNumber+1 #adds one to the variable photo nmber
    sense.show_message("Looping", text_colour = (255, 0, 0))
    sleep(55)#waits for 55 seconds
               

