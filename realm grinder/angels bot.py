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


def castSpells():
    pyautogui.moveTo(2390, 800)
    pyautogui.click(2355, 524)
    pyautogui.sleep(0.1)
    pyautogui.moveTo(2390, 800)
    pyautogui.click(2355, 472)
    pyautogui.sleep(0.1)
    pyautogui.moveTo(2390, 800)
    pyautogui.click(2355, 427)
    pyautogui.sleep(0.1)
    pyautogui.moveTo(2390, 800)
    pyautogui.click(2355, 375)
    pyautogui.sleep(0.5)
    pyautogui.moveTo(2390, 800)
    pyautogui.keyDown("ctrl")
    pyautogui.sleep(0.5)
    pyautogui.click(2355, 328)
    pyautogui.sleep(0.1)
    pyautogui.keyUp("ctrl")
    pyautogui.sleep(0.5)
    pyautogui.moveTo(2390, 800)
    pyautogui.sleep(0.1)
    timedClick(1.0)
    pyautogui.sleep(0.5)
    pyautogui.keyDown("ctrl")
    pyautogui.sleep(0.5)
    pyautogui.click(2355, 328)
    pyautogui.sleep(0.1)
    pyautogui.keyUp("ctrl")
    pyautogui.sleep(0.5)
    pyautogui.moveTo(2390, 800)
    pyautogui.sleep(0.1)


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
            r, g, b, = pyautogui.pixel(2347, 198)
            if b == 255:
                castSpells()


if __name__ == '__main__':
    asyncio.run(main())
