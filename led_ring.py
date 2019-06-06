from microbit import *
import neopixel
import time

num_pixels = 24
pixels = noepixel.NeoPixel(pin0, num_pixels)


def update_leds(r, g, b):
    global pixels
    for i in range(24):
        pixel[i] = (r, g, b)
        time.sleep_ms(10)
        pixels.show()

while True:
    
    updete_leds(255, 0, 0)
    sleep(2000)
    
    updete_leds(0, 255, 0)
    sleep(2000)
    