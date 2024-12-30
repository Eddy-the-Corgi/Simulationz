from selenium import webdriver
import pyautogui
import time
import sys

pyautogui.FAILSAFE = True

time.sleep(5)

#x, y = pyautogui.position()
#print((x,y))
#sys.exit()

for _ in range(150):
    pyautogui.moveTo(48, 212) # go to 48, -270 offset from 318
    pyautogui.hotkey('ctrl', 'shift', 'a')
    pyautogui.mouseDown()
    pyautogui.moveTo(1880, 992) # +270 offset from 1610, go to 1880
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('right')
    time.sleep(3)

#driver.quit()