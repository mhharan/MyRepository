from pyautogui import *
import time
FAILSAFE=False

query="say hi" #google search query

press("win")
time.sleep(2)
write("chrome")
press("enter")
time.sleep(2)
write("www.google.com")
press("enter")
time.sleep(3)
write(query)
press("enter")
