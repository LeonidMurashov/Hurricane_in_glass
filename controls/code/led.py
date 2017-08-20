import RPi.GPIO as GPIO
import time
import threading as T


pins = [32, 38, 36]
rgb = [0,0,0]
blinking = False
# 38 - green, 32 - red, 36 - blue

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    for i in pins:
        GPIO.setup(i,GPIO.OUT)
    light_led(0,0,0)
    thr = T.Thread(target=__blinker)
    thr.start()

def __blinker():
    while(True):
        if blinking:
            light_led(*rgb)
            time.sleep(0.5)
            light_led(0,0,0)
            time.sleep(0.5)

# Send boolean values
def blink(r,g,b):
    global rgb, blinking
    rgb = [r,g,b]
    blinking = True

def stop_blink():
    global blinking
    blinking = False

# Send here boolean values
def light_led(r,g,b):
    GPIO.output(pins[0],r)    
    GPIO.output(pins[1],g)    
    GPIO.output(pins[2],b)

def dispose():
    GPIO.cleanup()
