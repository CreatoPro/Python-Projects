from math import trunc
import os
from sys import path
import sys
from types import MappingProxyType
from urllib.parse import SplitResult
import pyttsx3
from selenium.webdriver.remote.webdriver import WebDriver
import speech_recognition as sr
import pyaudio
from speech_recognition import Microphone
import datetime
import cv2
import requests
import wikipedia
import random
import webbrowser
import pyautogui as pg
import pyjokes
import time
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import selenium
import requests
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from PyQt5.uic import loadUiType
from wikipedia.wikipedia import search
from RinkuUI import Ui_Rinku
import operator



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
chrome_path = r'C:\ Program Files (x86)\ Google\ Chrome\ Application\ chrome.exe %s'
googlenews = GoogleNews()




def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")




class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    # def run(self):
    #     self.Taskexecution      
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening.....')
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=5)
        try:
            print("Reconizing....")
            query = r.recognize_google(audio, language='en-in')
            if "wake up rinku" in query:
                speak('I am listening')
            print(f"User said: {query}\n")
            if "thank you" in query:
                speak('your welcome')
            if "hello rinku" in query:
                speak('hello, how are you')
            if "how are you" in query:
                speak('i am always fine, may I know how can i help you')
        except Exception as e:
            print("Say that again please....")
            return "None"
        query = query.lower()
        return query 
        
    def run(self):
        # self.Taskexecution()
        speak('please say wakeup Rinku to continue')
        while True:
            self.query = self.takecommand()
            if 'wake up' in self.query or 'are you there' in self.query or 'hello rinku' in self.query:
                self.Taskexecution()
            if 'terminate yourself' in self.query or 'rinku stop' in self.query:
                speak('thank you for talking to me. just start me if you need me')
                sys.exit()    
            

    def Taskexecution(self):
        wishMe()
        speak("Rinku Online")
        speak("Tell me, I am listening")
        while True:
        
            self.query = self.takecommand().lower()

            if "open notepad" in self.query:
                speak("nahi kholungee")
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)
            elif 'terminate yourself' in self.query or 'rinku stop' in self.query:
                speak('thank you for talking to me. just start me if you need me')
                sys.exit()  
            
            elif "sleep now" in self.query:
                speak('i am going to sleep. you can say wakeup to continue')
                break;
            # elif "how are you" in self.query():
            #     speak("i am always fine,may I know how can i help you")
            # elif "hello rinku" in self.query:
            #     speak('hello, how are you')
            elif 'temperature' in self.query:
                search = 'temperature here'
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp} ")

            elif(( "open command prompt" in self.query) or ( "open cmd" in self.query)):
                speak("Naahi")
                os.system("start cmd")
            elif"open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while(True):
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)            
                    k = cv2.waitKey(50)
                    if k==5:
                        break
                cap.release()
                cv2.destroyAllWindows()
            
            elif"close camera" in self.query:
                speak('closing camera')
                os.system("taskkill /f /im camera.exe")

            elif 'wikipedia' in self.query:
                speak('searching wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences = 2 )
                speak("According to wikipedia")
                print("results")
                speak(results)
            elif 'open google' in self.query:
                speak("OK")
                webbrowser.get(chrome_path)
                webbrowser.open_new_tab("www.google.com")
            elif 'start' in self.query:
                speak("OK")
                pg.moveTo(x=28, y=1052, duration=2)
                pg.click()
            elif 'close notepad' in self.query:
                speak('closing notepad')
                os.system("taskkill /f /im notepad.exe")
            elif 'tell me a joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            elif 'close chrome' in self.query:
                speak('closing chrome')
                os.system("taskkill /f /im chrome.exe")
            elif 'setup google excel' in self.query:
                speak("setting up google sheets")
                webbrowser.get(chrome_path)
                webbrowser.open_new_tab("https://www.google.com/docs/about/")
                time.sleep(3)
                pg.click(x=424, y=171, duration=1)
                pg.click(x=641, y=861, duration=1)
                time.sleep(2)
                pg.click(x=339, y=375, duration=1)
                speak('done')
            # elif 'inconito google' in query:
            #     speak("OK")
            #     webbrowser.get(chrome_incog).open_new('www.google.com')
            elif 'set up google ads' in self.query:
                speak("initializing google ads")
                chrome_incog = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
                webbrowser.get(chrome_incog).open_new('www.google.com')
                options=Options()
                options.add_argument("--start-maximized")
                pg.PAUSE = 2
                pg.moveTo(x=700, y=1063, duration=0.1)
                pg.click(x=832, y=975, duration=0.1)
                pg.hotkey('win','up')
                pg.PAUSE = 2
                pg.click(x=255, y=67, duration=0.2)
                pg.PAUSE = 2.5
                pg.typewrite('ads.google.com ', interval=0.2)
                pg.hotkey('enter')
                pg.PAUSE = 5
                pg.click(x=1620, y=248, duration=0.2)
                pg.click(x=788, y=524, duration=0.2)
                pg.typewrite('social@iigacademy.com', interval=0.1)
                pg.hotkey('enter')
                pg.PAUSE = 5
                pg.typewrite('Social@123IIGA', interval=0.1)
                pg.hotkey('enter')
                time.sleep(30)
                speak('setting up new campaign')
                pg.PAUSE = 5
                pg.click(x=619, y=413, duration=0.2)
                pg.click(x=693, y=462, duration=0.2)
                pg.PAUSE = 5
                speak('setting ads for website traffic')
                pg.click(x=1129, y=517,duration=3)
                speak('setting ads for search ads')
                pg.click(x=484, y=499, duration=0.2)
                pg.click(x=387, y=563, duration=0.2)
                pg.typewrite('www.iigacademy.com', interval=0.1)
                pg.click(x=314, y=883, duration=0.2)
                speak('done')
            elif 'open youtube' in self.query:
                chrome_driver = 'Users\\Shreesat\\Desktop\\chromedriver_win32' 
                driver = webdriver.Chrome(chrome_driver)
                webbrowser.open_new_tab("www.youtube.com")
                searchbox = driver.find_element_by_xpath('//*[@id="search"]')
                searchbox.send_keys('Shreesat Sahu')
            elif 'type what i say' in self.query:
                speak('Speak what you want to say')

            elif "do some calculations" in self.query or "can you calculate" in self.query:            
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' :operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                        }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                print(eval_binary_expr(*(my_string.split())))

            
            elif 'attend online classes' in self.query:
                speak("attending online classes")
                npath = r"F:\Python projects\Shreesat\Class Attender\Class_attender.py"
                os.startfile(npath)
            elif 'shutdown the sysytem' in self.query:
                speak('sorry I dont have the access to that')
            elif 'switch the window' in self.query:
                pg.keyDown('alt')
                pg.press('tab')
                time.sleep(1)
                pg.keyUp('alt')
            elif 'today news' in self.query:
                speak("wait sir, fetching latest news")
                engine.runAndWait()
                googlenews.get_news('Todays news')
                googlenews.result()
                a=googlenews.gettext()
                print(*a[1:5],sep=',')
                speak(f'{a}')
            elif "stop online classes" in self.query:
                speak('stopping classes')
                npath = r"F:\Python projects\Shreesat\Class Attender\Class_attender.py"
                os.system("taskkill /f /im py.exe")
            
            elif 'battery percentage' in self.query or 'battery percent' in self.query :
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f'our system has {percentage} percentage battery')
                if percentage ==100:
                    speak("battery is charging now")
                else:
                    speak ("please charge the system")
            
            elif 'internet speed' in self.query:
                import speedtest
                st= speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed')
                print(f'sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed')
                          
            
            elif "take a screenshot" in self.query:
                speak('please tell me the name in which you want to save the file')
                name=self.takecommand().lower()
                speak('please hold the screen for sometime, I am taking screenshot')
                time.sleep(3)
                img = pg.screenshot()
                img.save(f'{name}.png')
                speak('i am done, please give me next command')
            
            elif "type what i am saying" in self.query:
                speak('tell i am listening')
                def takecommands():
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            print('listening.....')
                            r.pause_threshold = 10
                            audio = r.listen(source, timeout=10, phrase_time_limit=5)
                            
                        try:
                            print("Typing....")
                            typing = r.recognize_google(audio, language='en-in')
                            if "wake up rinku" in typing:
                                speak('I am listening')
                            print(f"User said: {typing}\n")
                            if "thank you" in typing:
                                speak('your welcome')
                            if "hello rinku" in typing:
                                speak('hello, how are you')
                            if "how are you" in typing:
                                speak('i am always fine, may I know how can i help you')
                        except Exception as e:
                            print("Say that again please....")
                            return "None"
                        return typing
                typing=takecommands().lower()
                pg.typewrite(f'{typing}')
                speak('done')

                               


startExecution = MainThread() 

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Rinku()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.StartTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def StartTask(self):
        # self.ui.movie = QtGui.QMovie(r"F:\Python projects\Shreesat\Gui\Images\d8sothe-cb2ea492-6d7f-4916-a9bd-4088abfa0103.gif")
        self.ui.movie = QtGui.QMovie(r"Shreesat\d8sothe-cb2ea492-6d7f-4916-a9bd-4088abfa0103.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
        
app = QApplication(sys.argv)
Rinku = Main()
Rinku.show()
sys.exit(app.exec_())



       


            



            











