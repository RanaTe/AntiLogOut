import board
import time
import random
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard

mouse = Mouse(usb_hid.devices)

goright=True

while True:

    #2 parts to sequence, move mostly right, then mostly left

    #   set up for big move
    #longwait=random.randint(250,350)
    longwait=random.randint(2,3)
    bigoffsetx=random.randint(-10,10)
    bigoffsety=random.randint(-7,7)
        
#   	do 1st big move
    if goright:
    # do a right move
        print("moving right")
        mouse.move(100+bigoffsetx,bigoffsety)
        goright=False
    else:
    # do a left move
        print("moving left")
        mouse.move(-100+bigoffsetx,bigoffsety)
        goright=True

#		do some quick clicks and moves
    numberofclicks=random.randint(3,6)
    print("doing some clicks")
    for ismall in range(1,numberofclicks):
        #shortwait in ms (double click is usually less than 500ms)
        shortwait=0.001*random.randint(250,600)
        #print(shortwait)
        shortmovex=random.randint(-9,9)
        shortmovey=random.randint(-7,7)
        #move, wait, click
        mouse.move(shortmovex,shortmovey)
        time.sleep(shortwait)
        mouse.click(Mouse.LEFT_BUTTON)

    time.sleep(longwait)
    print("waiting for next move")
