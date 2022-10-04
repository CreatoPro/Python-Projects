import ntpath
from platform import system
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyautogui as pg
import datetime
import time
import os
import sys
from sys import path
import time
from datetime import date
import schedule
import webbrowser
from speech_recognition import Microphone
import pyttsx3
import pyaudio




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
driver_path = (r"F:\Python projects\Python-Projects\Shreesat\chromedriver_win32\chromedriver.exe")

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def friday6():
        # speak('attending online class in 3')
        # pg.PAUSE=0.2
        # speak('2')
        # pg.PAUSE=0.2
        # speak('1')
        chrome_path = r'C:\ Program Files (x86)\ Google\ Chrome\ Application\ chrome.exe %s'
        webbrowser.get(chrome_path)
        webbrowser.open_new_tab("https://teams.microsoft.com/l/meetup-join/19%3a3aRBPjge52Es8-aJ4E6JuhQgIflo9E6ryL4FOk6xVik1%40thread.tacv2/1641807045817?context=%7b%22Tid%22%3a%2234bd8bed-2ac1-41ae-9f08-4e0a3f11706c%22%2c%22Oid%22%3a%22fa47fa55-8668-4bf9-bae2-8efab29b045e%22%7d")
        time.sleep(4)
        pg.hotkey('win','down')
        pg.hotkey('win','up')
        pg.hotkey('enter')
        pg.click(x=1221, y=526, duration=2)
        pg.PAUSE=4
        time.sleep(10)       
        pg.click(x=944, y=659, duration=2)
        pg.click(x=960, y=619,duration=2)
        pg.press('volumeup',50)
        speak("Wakeup Rinku, Class has started")
        speak("Wakeup")
        speak("Wakeup")
        speak("Wakeup")
        speak("Wakeup")
        speak("Wakeup")
        speak("Wakeup")
        speak("Wakeup")
        speak("Wakeup")
        speak("Wakeup")

friday6()        

 
 



#for friday
# schedule.every().tuesday.at('11:55').do(friday6)






while True:
    schedule.run_pending()
    time.sleep(1)

