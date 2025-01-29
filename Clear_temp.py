import time
import pyautogui
import os
import shutil

path=r"C:\Users\NAVEEN\AppData\Local\Temp"
for file in os.listdir(path):
    address=os.path.join(path,file)
    try:
       if os.path.isfile(address):
          os.remove(address)
       elif os.path.isdir(address):
          shutil.rmtree(address)
    except Exception as e:
        print(f"{file}")
time.sleep(1)
pyautogui.hotkey("win", "d")
pyautogui.moveTo(900, 300)
time.sleep(1)
pyautogui.press('f5',presses=3)
time.sleep(1)
pyautogui.hotkey("win", "d")