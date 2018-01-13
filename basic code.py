##  IMPORTING MODULES ##
from picamera import PiCamera # Importing Pi camere module
from time import sleep # Importing command sleep
from sense_hat import SenseHat # Importing senes hat module
from PIL import Image # Importing Pillow a image processing module
import datetime as dt # Importing datetime module to give accurate date and time info
import ephem # Iss tracking library
import math # Imports python's math library


## VARIABLES ##
name = 'ISS (ZARYA)' # Iss Data             
line1 = '1 25544U 98067A   18011.65344505  .00003116  00000-0  53990-4 0  9994'
line2 = '2 25544  51.6426  79.0696 0003478   2.6590 144.2138 15.54293905 94174'
threshold =  120 # A set threshold for the RGB Value of White
thresholdB = 10 # A set threshold for the RGB Value of Black
sense = SenseHat() # Making sense hat's name shorter
camera = PiCamera() # Making the cameras name shorter
b = [0, 0, 255] # Blue sense hat pixels
g = [0, 255, 0] # Green pixels on sense hat
PhotoNumber = 1 # Variable to store the n.o of the photo that has been taken
iss = ephem.readtle(name, line1, line2) # Puts data to ephem
sun = ephem.Sun() # Imports ephem's sun as sun
twilight = math.radians(-6)
time = dt.datetime.now().strftime("%H:%M:%S") # Gets the current time and arranges it into a redable format
## MAIN CODE ##

for i in range(10):
    ## VARIABLES ##
    w = 49 # Variable to store width of photo
    h = 49 # Variable to store height of photo
    x = 1.0 # Variable to store X value
    y = 1.0 # Variable to store Y value
    white_pixels = 0 # Variable to store n.o of white pixels
    other_pixels = 0 # Variable to store n.o of non black & white pixels
    black_pixels = 0 # Variable to store n.o of black pixels
    blank = [              # Sense hat images to show % cloud cover to astronauts
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
        ]
    
    one = [              
        g,g,g,g,g,g,g,g,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
        ]
    two = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
        ]
    three = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
        ]
    four = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
        ]
    five = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
        ]
    six = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b
        ]
    seven = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        b,b,b,b,b,b,b,b
        ]
    eight = [
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g,
        g,g,g,g,g,g,g,g
        ]
    ## TRACKING ISS ###
    
    iss.compute() # Gets iss tle data
    
    obs = ephem.Observer()
    
    obs.lat = iss.sublat
    obs.long = iss.sublong
    obs.elevation = 0
    sun.compute(obs)
    sun_angle = math.degrees(sun.alt)
    day_or_night = 'Day' if sun_angle > twilight else 'Night'
    print("Lat %s - Long %s" % (iss.sublat, iss.sublong))
    latlong = ("Lat %s - Long %s" % (iss.sublat, iss.sublong))
    lat = iss.sublat
    long = iss.sublong
    issheight = ("ISS height %d" %iss.elevation)
    ISSheight = iss.elevation
    if day_or_night == 'Night':
        sense.show_message("It is night now Time: %s" %time)
    else:
        sense.show_message("Hello", text_colour = (0, 255, 0)) # Displaying hello in green on Sense Hat

        ## Taking a Picture ##

        str_time = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") # Gets the current date and time and arranges it into a redable format

        text = latlong + " " + str_time + " " + issheight 
        with open('long.txt', 'w') as f:
            f.write(('Lat %s - Long %s time %s ISS Height %s' + '/n') %(lat, long, str_time, ISSheight))
        camera.annotate_text = text # Add the date and time to the image
        camera.start_preview() 
        sleep(5)
        camera.capture('/home/pi/AstroPi/ColourIndex(%d).jpg' %PhotoNumber) # Takes a picture and calls it ColourIndex + the n.o of photo

        camera.resolution = (50, 50) # Sets camera resolution to 50x50 pixels
        sleep(5)    
        camera.capture('/home/pi/AstroPi/CloudCover(%d).jpg' %PhotoNumber)# Takes a photo and calls it CloudCover then the n.o of photo
        camera.stop_preview()

        sense.show_message("Picture Taken", text_colour = (0, 0, 255)) # Displays the message picture taken on the sense hats matrix
         
        ### Cloud Cover Processing ###



        im = Image.open('CloudCover(%d).jpg' %PhotoNumber) # Opens a spesifice Cloud Cover image
        rgb_im = im.convert('RGB') # Converts the image to RGB


        while y<=h: # Check's it is in the boundary of the photo
            while True: # An Infante loop
                    r, g, b = rgb_im.getpixel((x, y)) # Gets a spesific pixels RGB values
                    if b and r and g >= threshold: # Sees if the total RGB value is larger or equal to the white threshold
                        white_pixels += 1 # If that equals yes add one to the white_pixels variable
                    elif b and r and g <= thresholdB:  # Decides if the pixel is black
                        black_pixels += 1
                    else:
                        other_pixels += 1
                    print(r, g, b)
                    x += 1
                    if x > w:
                        x=1
                        break
            y += 1
        percent_cover = (white_pixels/(white_pixels+other_pixels))*100 # Calculates the percent cover of the cloud
        print(black_pixels) # Prints the n.o. black pixels
        print(white_pixels) # Prints the n.o. white pixels
        print(other_pixels) # Prints the n.o. other pixels
        percent_cover = (white_pixels/(white_pixels+other_pixels))*100 # A calculation to work out the % of the sky that was covered by cloud
        print("Percent cover: %d" %percent_cover) # Prints the % of the sky covered by the cloud
        if white_pixels < 12.5:# If there are more than 1 white pixel then do this
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100]) # Shows a picture depending on the % of cloud cover in the picture
            sense.set_pixels(blank)
        else:
            print("Percent cover: %d" %percent_cover) # Prints the % of the sky covered by the cloud
        if percent_cover <= 24:
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100])
            sense.set_pixels(one)
        elif percent_cover <= 36.5:
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100])
            sense.set_pixels(two)
        elif percent_cover <= 49:
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100])
            sense.set_pixels(three)
        elif percent_cover  <= 61.5:
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100])
            sense.set_pixels(four)
        elif percent_cover <= 74:
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100])
            sense.set_pixels(five)
        elif percent_cover <= 86.5:
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100])
            sense.set_pixels(six)
        elif percent_cover <= 99:
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100])
            sense.set_pixels(seven)
        else:
            sense.show_message("1 green row = 12.5% Cloud cover all blue rows = <12.5% Cloud cover", text_colour=[0,100,100])
            sense.set_pixels(eight)
        

    PhotoNumber = PhotoNumber+1 # Adds one to the variable photo nmber
    sleep(60) # Waits for 60 seconds
                   

