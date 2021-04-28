import keyboard
import pyautogui as pg
from time import *
sleep(2)
def MagicPianoBot():
    #4 columns: (762, 400), (798, 400), (881, 400), (949, 400)
    while keyboard.is_pressed('q') == False:
        if pg.pixel(762, 400)[0] == 0:
            pg.mouseDown(762, 400)
        if pg.pixel(798, 400)[0] == 0:
            pg.mouseDown(798, 400)
        if pg.pixel(881, 400)[0] == 0:
            pg.mouseDown(881, 400)
        if pg.pixel(949, 400)[0] == 0:
            pg.mouseDown(949, 400)
#rgb(255,242,234)
def PositionCursor():
    #(634, 328) --- (1270, 843)
    while keyboard.is_pressed('q') == False:
        pg.sleep(2)
        print(pg.position())
def AimBoost():
    while keyboard.is_pressed('q') == False:
        pic = pg.screenshot(region=(660, 350, 740, 520))
        w, h = pic.size
        for x in range(0, w, 5):
            for y in range(0, h, 5):
                r, g, b = pic.getpixel((x, y))
                if b == 195:
                    pg.mouseDown(x + 660, y + 350)
                    pg.sleep(0.1)
                    break

