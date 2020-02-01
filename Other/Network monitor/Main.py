#Imports
import time
import signal

import socket # For Pinging
from urllib2 import urlopen, URLError, HTTPError # For pinging

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw

#Inital Variables
text = ('Booting..')
router = 0
dnspi = 0
internet = '1'
backlightr = "0"

#Inital Backlight set
backlight.set_pixel(2, 0, 255, 0) #Backlight colour (I think first is brightness, 0-5, then RGB)
backlight.show()

#Write pixels function
def write(text):
    led_states = [False for _ in range(6)]
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 25)
    #Make sure to set the text variable
    w, h = font.getsize(text)
    x = (width - w) // 2
    y = (height - h) // 2
    draw.text((x, y), text, 1, font)
    ## Plot the pixels
    for x in range(128):
        for y in range(64):
            pixel = image.getpixel((x, y))
            lcd.set_pixel(x, y, pixel)
    #Display the pixels
    lcd.show()

#Console Output
print('Network Monitor Online')

##NETWORKING - PINGING & TESTING

def pingint():
    socket.setdefaulttimeout( 23 )
    global internet # This makes internet a global variable so the rest of the program can see the changes.
    try :
        response = urlopen('https://google.com')
    except HTTPError, e:
        print 'The server couldn\'t fulfill the request. Reason:', str(e.code)
        internet = "0"
    except URLError, e:
        print 'We failed to reach a server. Reason:', str(e.reason)
        internet = "0"
    except Exception, e:
        internet = "0"
        print('Except exception')
    else :
        internet = "1"
        # do something, turn the light on/off or whatever


def pingdns():
    socket.setdefaulttimeout( 23 )
    global dnspi # This makes dnspi a global variable so the rest of the program can see the changes.
    try :
        response = urlopen('http://192.168.1.127')
    except HTTPError, e:
        print 'The server couldn\'t fulfill the request. Reason:', str(e.code)
        dnspi = "0"
    except URLError, e:
        print 'We failed to reach a server. Reason:', str(e.reason)
        dnspi = "0"
    else :
        dnspi = "1"
        # do something, turn the light on/off or whatever

def pingrouter():
    socket.setdefaulttimeout( 23 )
    global router # This makes router a global variable so the rest of the program can see the changes.
    try :
        response = urlopen('http://192.168.1.254')
    except HTTPError, e:
        print 'The server couldn\'t fulfill the request. Reason:', str(e.code)
        router = "0"
    except URLError, e:
        print 'We failed to reach a server. Reason:', str(e.reason)
        router = "0"
    else :
        router = "1"
        # do something, turn the light on/off or whatever

def testfor():
    #pingint() #Temporarily disabled. kept getting blocked for DDOSing.
    pingdns()
    pingrouter()
    #Logic
    if router == "1":
        if dnspi == "1":
            if internet == "1":
                write(time.strftime("%I:%M:%S"))  #Possibly change to time?
                backlight.set_all(0, 255, 0) #Backlight colour (I think first is brightness, 0-5, then RGB)
                backlight.show()
            else:
                write('Internet Fail')
                print('Internet Fail')
                backlightr = "1" # Used to determine if the backlight should be refreshed on turning back green
                backlight.set_all(255, 0, 0) #Backlight colour (I think first is brightness, 0-5, then RGB)
                backlight.show()
        else:
            write("DNS-PI FAIL")
            print('DNS-PI FAIL')
            backlightr = "1" # Used to determine if the backlight should be refreshed on turning back green
            backlight.set_all(255, 0, 0) #Backlight colour (I think first is brightness, 0-5, then RGB)
            backlight.show()
    else:
        write("ROUTER FAIL")
        print('Router fail')
        backlightr = "1" # Used to determine if the backlight should be refreshed on turning back green
        backlight.set_all(255, 0, 0) #Backlight colour (I think first is brightness, 0-5, then RGB)
        backlight.show()


write("Connecting...")

def internet_on():
    while 0 == 0:
        backlight.set_all(55, 118, 199) #Backlight colour (I think first is brightness, 0-5, then RGB)
        backlight.show()
        try:
            urllib2.urlopen('http://192.168.1.254', timeout=5)
            xyf = "1"
        except urllib2.URLError as err: 
            xyf = "0"
            backlight.set_all(41, 89, 152) #Backlight colour (I think first is brightness, 0-5, then RGB)
            backlight.show()
        if xyf == "1":
            break



#Main Loop
while 0 == 0:
    testfor()
