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

def zoom():
        pg.hotkey('win')
        pg.typewrite('zoom')
        pg.hotkey('enter')

def monday1():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/99685007041?pwd=bkVmZ1oxdTJ1ZVRRWUhMdVY2WEUxZz09")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def monday2():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/91248532136")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def monday3():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/94599816971")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        pg.PAUSE=10
        pg.click(x=793, y=464,duration=1)
        pg.typewrite('309779')
        pg.PAUSE=3
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def monday5():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/94704903516")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def monday6():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/91574406786")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def tuesday2():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/97927971024")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.click(x=793, y=464,duration=1)
        pg.typewrite('123345')
        pg.PAUSE=3
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def tuesday3():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/92986165933")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def tuesday5():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/99193414680")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        pg.PAUSE=10
        pg.click(x=793, y=464,duration=1)
        pg.typewrite('432891')
        pg.PAUSE=3
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        
        

def tuesday6():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/96902894526")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        pg.PAUSE=10
        pg.click(x=793, y=464,duration=1)
        pg.typewrite('658106')
        pg.PAUSE=3
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def wednesday3():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/99054650988?pwd=cldEbmFOblVDNVU4VXN2cmJ3ZlQ4QT09")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        
#for microsoft teams
def wednesday6():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        chrome_path = r'C:\ Program Files (x86)\ Google\ Chrome\ Application\ chrome.exe %s'
        webbrowser.get(chrome_path)
        webbrowser.open_new_tab("https://teams.microsoft.com/l/meetup-join/19%3arb8tSGfFeuv9ZHlvF-_IxlTsMvSgBnG2AOwyatT8eKE1%40thread.tacv2/1629196570183?context=%7b%22Tid%22%3a%2234bd8bed-2ac1-41ae-9f08-4e0a3f11706c%22%2c%22Oid%22%3a%22ebe0900c-9df1-442d-9af1-a33e77beb7e1%22%7d")
        time.sleep(4)
        pg.click(x=1234, y=274,duration=2)
        pg.click(x=1221, y=526, duration=2)
        pg.PAUSE=4
        time.sleep(10)       
        pg.click(x=944, y=717, duration=2)
        pg.click(x=954, y=660,duration=2)

def thursday1():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/99552508836")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        
def thursday2():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/96469605848")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        pg.PAUSE=10
        pg.click(x=793, y=464,duration=1)
        pg.typewrite('034517')
        pg.PAUSE=3
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        
def thursday3():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        driver.get("https://cuchd-in.zoom.us/j/96765281388?pwd=Y3Z1Y0ptdGkrd2FhMlZaUzRPZkNXZz09")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        

def thursday6():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        chrome_path = r'C:\ Program Files (x86)\ Google\ Chrome\ Application\ chrome.exe %s'
        webbrowser.get(chrome_path)
        webbrowser.open_new_tab("https://teams.microsoft.com/l/meetup-join/19%3arb8tSGfFeuv9ZHlvF-_IxlTsMvSgBnG2AOwyatT8eKE1%40thread.tacv2/1629196603927?context=%7b%22Tid%22%3a%2234bd8bed-2ac1-41ae-9f08-4e0a3f11706c%22%2c%22Oid%22%3a%22ebe0900c-9df1-442d-9af1-a33e77beb7e1%22%7d")
        time.sleep(4)
        pg.click(x=1234, y=274,duration=2)
        pg.click(x=1221, y=526, duration=2)
        pg.PAUSE=4
        time.sleep(10)       
        pg.click(x=944, y=717, duration=2)
        pg.click(x=954, y=660,duration=2)

def friday6():
        chrome_path = r'C:\ Program Files (x86)\ Google\ Chrome\ Application\ chrome.exe %s'
        webbrowser.get(chrome_path)
        webbrowser.open_new_tab("https://teams.microsoft.com/l/meetup-join/19%3arb8tSGfFeuv9ZHlvF-_IxlTsMvSgBnG2AOwyatT8eKE1%40thread.tacv2/1629196645520?context=%7b%22Tid%22%3a%2234bd8bed-2ac1-41ae-9f08-4e0a3f11706c%22%2c%22Oid%22%3a%22ebe0900c-9df1-442d-9af1-a33e77beb7e1%22%7d")
        time.sleep(4)
        pg.click(x=1234, y=274,duration=2)
        pg.click(x=1221, y=526, duration=2)
        pg.PAUSE=4
        time.sleep(10)       
        pg.click(x=944, y=717, duration=2)
        pg.click(x=954, y=660,duration=2)
def friday7():
        speak('attending online class in 3')
        pg.PAUSE=0.2
        speak('2')
        pg.PAUSE=0.2
        speak('1')
        driver = webdriver.Chrome(driver_path)
        # driver.maximize_window()
        driver.get("https://cuchd-in.zoom.us/j/94266154091?pwd=NnJDTGJLL245MERhRVV1TStnQkJrQT09")
        pg.hotkey('win','up')
        pg.hotkey('left')
        pg.hotkey('enter')
        time.sleep(10)
        pg.hotkey('enter')
        
zoom()     
friday7()   
#for monday
# schedule.every().monday.at('09:45').do(monday1)
# schedule.every().monday.at('10:35').do(monday2)
# schedule.every().monday.at('11:25').do(monday3)
# schedule.every().monday.at('13:05').do(monday5)
# schedule.every().monday.at('13:55').do(monday6)
# #for tuesday
# schedule.every().tuesday.at('10:35').do(tuesday2)
# schedule.every().tuesday.at('11:25').do(tuesday3)
# schedule.every().tuesday.at('13:05').do(tuesday5)
# schedule.every().tuesday.at('13:55').do(tuesday6)
# #for wednesday
# schedule.every().wednesday.at('11:25').do(wednesday3)
# schedule.every().wednesday.at('13:55').do(wednesday6)
# #for thursday
# schedule.every().thursday.at('09:45').do(thursday1)
# schedule.every().thursday.at('10:35').do(thursday2)
# schedule.every().thursday.at('11:25').do(thursday3)
# schedule.every().thursday.at('13:55').do(thursday6)
# #for friday
# schedule.every().friday.at('13:55').do(friday6)
# schedule.every().friday.at('14:45').do(friday7)





# while True:
#     schedule.run_pending()
#     time.sleep(1)


