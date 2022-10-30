import webbrowser
import pyautogui, webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+34693701753")

sleep(15) # esperamos 15 segundos para que se abra la web

with("text.txt","r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")