import cv2
import numpy as np
import copy
from utils import TemplateMatcher, Bot, Action
import pyautogui
import time
import keyboard

def get_action_for_state(img, bots):
    for b in bots:
        match = b.match_image(img, threshold=0.55)

        if match:
            return b.action
    
    return None


bot_down = Bot(TemplateMatcher(template=cv2.imread("templates/down_cropped.png", 0)), Action.DOWN)
bot_up= Bot(TemplateMatcher(template=cv2.imread("templates/up_cropped.png", 0)), Action.UP)
bot_back = Bot(TemplateMatcher(template=cv2.imread("templates/back_cropped.png", 0)), Action.BACK)

bots = [bot_down, bot_up, bot_back]

QUIT = False # We loop in-game until this is set to True.

CAPTURE_AREA = ((1000, 550), (1200, 780))

def terminate_program():
    global QUIT
    
    QUIT = True
    
    exit(0)

keyboard.add_hotkey('c', terminate_program)

while not QUIT:
    img = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)[CAPTURE_AREA[0][1]:CAPTURE_AREA[1][1], CAPTURE_AREA[0][0]:CAPTURE_AREA[1][0]]

    key = get_action_for_state(img, bots)

    if key:
        if key == Action.BACK:
            time.sleep(0.5)
        else:
            time.sleep(0.125)#0.125

        pyautogui.press(key)
        time.sleep(0.0625)
