import time
import asyncio
import pyautogui
import keyboard

# check color of pixel at 2347, 201
# click on pixel at 2355, 375
# click on pixel at 2355, 472
# click on pixel at 2355, 424 if possible
# move mouse to pixel at 2390, 800

pyautogui.PAUSE = 0.0
time.sleep(2)

async def timedClick(duration):
    t_end = time.time() + duration
    while time.time() < t_end:
        pyautogui.click()
        pyautogui.sleep(0.055)

async def click():
    pyautogui.click()
    await asyncio.sleep(0.055)

async def castGrandBalance():
    r, g, b, = pyautogui.pixel(2347, 201)
    if b == 255:
        pyautogui.click(2355, 375)
        pyautogui.moveTo(2390, 800)
        await timedClick(8.0)
        # await asyncio.sleep(8.0)
        pyautogui.click(2355, 472)
        pyautogui.moveTo(2390, 800)
        await timedClick(1.0)
        # await asyncio.sleep(1.0)
        pyautogui.click(2355, 328)
        pyautogui.moveTo(2390, 800)
        await timedClick(0.1)
        # await asyncio.sleep(0.1)
        pyautogui.click(2355, 328)
        pyautogui.moveTo(2390, 800)
        await timedClick(0.1)
        # await asyncio.sleep(0.1)
        pyautogui.click(2355, 328)
        pyautogui.moveTo(2390, 800)

async def main():
    clicking = False
    while not keyboard.is_pressed("q"):
        if keyboard.is_pressed("c"):
            clicking = not clicking
            pyautogui.sleep(0.5)
        if clicking:
            castingTask = asyncio.create_task(castGrandBalance())
            clickingTask = asyncio.create_task(click())
            # await castingTask
            await clickingTask

if __name__ == '__main__':
    asyncio.run(main())
