import time
import pyautogui
import keyboard

pyautogui.PAUSE = 0.055
time.sleep(2)

clicking = False
while not keyboard.is_pressed("q"):
    if keyboard.is_pressed("c"):
        clicking = not clicking
        pyautogui.sleep(0.4)
    if clicking:
        pyautogui.click()
