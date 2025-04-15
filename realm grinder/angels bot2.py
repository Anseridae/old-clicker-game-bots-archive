import time
import asyncio
import pyautogui
import keyboard
from threading import Timer

pyautogui.PAUSE = 0.0
time.sleep(2)

timerExists = False
clicking = False


def timedClick(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        pyautogui.click()
        pyautogui.sleep(0.055)


async def click():
    pyautogui.click()
    await asyncio.sleep(0.055)


def buyBuildings():
    if clicking:
        pyautogui.sleep(0.1)
        pyautogui.click(2555, 770)
        pyautogui.sleep(0.1)
        pyautogui.click(2555, 830)
        pyautogui.sleep(0.1)
        pyautogui.click(2555, 710)
        pyautogui.sleep(0.1)
        for x in range(660, 230, -60):
            pyautogui.click(2555, x)
            pyautogui.sleep(0.1)
        pyautogui.moveTo(2390, 800)
        global timerExists
        timerExists = False


async def main():
    global timerExists
    global clicking
    while not keyboard.is_pressed("q"):
        if keyboard.is_pressed("c"):
            clicking = not clicking
            pyautogui.sleep(0.5)
        if clicking:
            if not timerExists:
                timerExists = True
                t = Timer(180.0, buyBuildings)
                t.daemon = True
                t.start()
            clickingTask = asyncio.create_task(click())
            await clickingTask

if __name__ == '__main__':
    asyncio.run(main())
