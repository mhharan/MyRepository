import pyautogui
import cv2
pyautogui.FAILSAFE = True

pyautogui.dragTo(1095, 568, 2)
pyautogui.click(1095, 568, 5) #De 0,01 knop
pyautogui.dragTo(720, 644, 2)
pyautogui.click(720, 644) #De ct knop
if pyautogui.locateOnScreen("locate.png"): ##, confidence=0.4, region=(1220, 487, 32, 30)):
    x,y=pyautogui.locateCenterOnScreen("locate.png")
    pyautogui.doubleClick(x,y) #De clear knop
