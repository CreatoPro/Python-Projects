# from asyncio.timeouts import timeout
from math import trunc
import os
from socket import timeout
from subprocess import run
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
import pywhatkit
import pyperclip
from pytube import YouTube
from pywikihow import WikiHow, search_wikihow
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews
import operator
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
chrome_path = r'C:\ Program Files (x86)\ Google\ Chrome\ Application\ chrome.exe %s'
googlenews = GoogleNews()

battery = psutil.sensors_battery()
percentage = battery.percent




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


def YoutubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    webbrowser.get(chrome_path)
    webbrowser.open_new_tab(result)
    speak("this is what i found for your search .")
    pywhatkit.playonyt(term)
    speak('this may also help you sir .')
def DownloadYouTubeVideo():
    time.sleep(2)
    pg.click(x=429, y=65,duration=1)
    pg.hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value)
    
def Download(link):
    url = YouTube(link)
    video = url.streams.first()
    video.download(r'F:\Python projects\Python-Projects\Shreesat\Database\Youtube')
    speak("downloading video")
    Download(link)
    speak('done with downloading, check the video')
    os.startfile(r'F:\Python projects\Python-Projects\Shreesat\Database\Youtube')

   
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(1) as source:
        print('listening.....')
        r.pause_threshold = 1
        # audio = r.listen(source, timeout=1, phrase_time_limit=5,)
        audio = r.listen(source, timeout=6)

    try:
        print("Reconizing....")
        query = r.recognize_google(audio, language='en-in')
        if "wake up" in query:
            speak('Yes')
        print(f"User said: {query}\n")
        if "thank you" in query:
            speak('your welcome')
        if "hello " in query:
            speak('hello, how are you')
        if "how are you" in query:
            speak('i am always fine, may I know how can i help you')
    except Exception as e:
        print("Say that again please....")
        return "None"
    query = query.lower()
    return query 
        
def run():
    # Taskexecution()
    speak('please say wake up Aleena to continue')
    while True:
        query = takecommand()
        if 'wake up' in query or 'are you there' in query or 'hello elina' in query:
            Taskexecution()
        if 'terminate yourself' in query or 'rinku stop' in query:
            speak('thank you for talking to me. just start me if you need me')
            sys.exit()    
            

def Taskexecution():
    wishMe()
    # speak("Aleena Online")
    # speak(f"Welcome Back, please wait I am checking systems. Our system has {percentage} percent battery. All processes are running fine")
    # speak("Tell me, How can I help you")
    while True:
    
        query = takecommand().lower()

        if "open notepad" in query:
            speak("nahi kholungee")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'terminate yourself' in query or 'elina stop' in query:
            speak('thank you for talking to me. just start me if you need me')
            sys.exit()  
        
        elif "sleep now" in query:
            speak('i am going to sleep. you can say wakeup to continue')
            break;
        # elif "how are you" in query():
        #     speak("i am always fine,may I know how can i help you")
        # elif "hello rinku" in query:
        #     speak('hello, how are you')
        elif 'temperature here' in query:
            search = query
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp} ")

        elif(( "open command prompt" in query) or ( "open cmd" in query)):
            speak("Naahi")
            os.system("start cmd")
        elif"open camera" in query:
            cap = cv2.VideoCapture(0)
            while(True):
                ret, img = cap.read()
                cv2.imshow('webcam', img)            
                k = cv2.waitKey(50)
                if k==5:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "youtube search" in query:
            Query = query.replace("rinku","")
            query=Query.replace("youtube search","")
            YoutubeSearch(query)  
        elif "download this video" in query:
            DownloadYouTubeVideo()  
                        
        elif"close camera" in query:
            speak('closing camera')
            os.system("taskkill /f /im camera.exe")

        elif 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2 )
            speak("According to wikipedia")
            print("results")
            speak(results)
        elif 'open google' in query:
            speak("OK")
            webbrowser.get(chrome_path)
            webbrowser.open_new_tab("www.google.com")
        elif 'start' in query:
            speak("OK")
            pg.moveTo(x=28, y=1052, duration=2)
            pg.click()
        elif 'close notepad' in query:
            speak('closing notepad')
            os.system("taskkill /f /im notepad.exe")
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)
        elif 'close chrome' in query:
            speak('closing chrome')
            os.system("taskkill /f /im chrome.exe")
        elif 'setup google excel' in query:
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
        elif 'set up google ads' in query:
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
            pg.typewrite('', interval=0.1)
            pg.hotkey('enter')
            pg.PAUSE = 5
            pg.typewrite('', interval=0.1)
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
        # elif 'open youtube' in query:
        #     chrome_driver = r'Shreesat\chromedriver_win32\chromedriver.exe' 
        #     driver = webdriver.Chrome(chrome_driver)
        #     driver.get("https://www.youtube.com")
        #     searchbox = driver.find_element_by_xpath('//*[@id="search"]')
        #     searchbox.send_keys('Shreesat Sahu')
        elif 'type what i say' in query:
            speak('Speak what you want to say')

        elif "what is" in query or "what do you mean by" in query:
                query = query.replace("what is","")
                query = query.replace("what do you mean by","")
                pywhatkit.search(query)
                search = wikipedia.summary(query,1)
                speak(f"According to your search {search}")

        elif "how to " in query:
            query = query.replace("how to","")
            pywhatkit.search(query)
            max_result = 1
            how_to_func = search_wikihow(query, max_results = max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
        elif "what are" in query:
            query = query.replace("what are","")
            pywhatkit.search(query)
            search = wikipedia.summary(query,1)
            speak(f"According to your search {search}")

        elif "do some calculations" in query or "can you calculate" in query:            
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

        
        elif 'attend online classes' in query:
            speak("attending online classes")
            npath = r"F:\Python projects\Python-Projects\Shreesat\Class Attender\Class_attender.py"
            os.startfile(npath)
                
        elif 'shutdown the system' in query:
            speak('sorry I dont have the access to that')
        elif 'switch the window' in query:
            pg.keyDown('alt')
            pg.press('tab')
            time.sleep(1)
            pg.keyUp('alt')
        elif 'today news' in query:
            speak("wait sir, fetching latest news")
            engine.runAndWait()
            googlenews.get_news('Todays news')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')
            speak(f'{a}')
        elif "stop online classes" in query:
            speak('stopping classes')
            npath = r"F:\Python projects\Python-Projects\Shreesat\Aleenawithouthui.py"
        elif 'battery percentage' in query or 'battery percent' in query :
            batterys = psutil.sensors_battery()
            charge = batterys.percent

            speak(f'our system has {charge} percentage battery')
            if charge ==100:
                speak("battery is charging now")
            else:
                speak ("please charge the system")
        
        elif 'internet speed' in query:
            speak('checking, please wait')
            import speedtest
            st= speedtest.Speedtest()
            dl = st.download()
            mb_dl = int(int(dl/80000))
            up = st.upload()
            mb_up = int(int(dl/80000))
            speak(f'sir we have {mb_dl} M B per second downloading speed and {mb_up} M B per second uploading speed')
            print(f'sir we have {mb_dl} M B per second downloading speed and {mb_up} M B per second uploading speed')
                        
        
        elif "take a screenshot" in query:
            speak('please tell me the name in which you want to save the file')
            name=takecommand().lower()
            speak('please hold the screen for sometime, I am taking screenshot')
            time.sleep(3)
            img = pg.screenshot()
            img.save(f'{name}.png')
            speak('i am done, please give me next command')
        
        elif 'mute' in query or 'unmute' in query:                
            pg.hotkey("volumemute")
            speak('Ok')
        elif 'pause the video' in query or 'play' in query:
            pg.press('k')
        elif 'press enter' in query:
            pg.hotkey('enter')
        elif 'close the current tab' in query : 
            speak('ok')
            pg.hotkey('ctrl','w') 
        elif 'close the tab' in query: 
            speak('ok')
            pg.hotkey('ctrl','w') 
        elif 'increase the volume' in query:
            pg.press('volumeup',5)
        elif 'decrease the volume' in query:
            pg.press('volumedown',3)
        elif 'next video' in query:
            pg.hotkey('shift','n')

        elif 'open system app' in query:
            speak('which app do you want me to open')
            app = takecommand()
            pg.hotkey('win')
            pg.typewrite(f'{app}')
            time.sleep(2)
            pg.hotkey('enter')
            speak('opening')
        elif 'close the current app' in query:
            speak('closing')
            pg.hotkey('alt','f4')

        elif "activate code 001" in query or "activate code zero zero one" in query:
            speak('shutting down the system, with the system I will also terminate')
            speak('are you sure, please answer in yes or no')
            
            while True:
                answer = takecommand()
                if 'yes' in answer: 
                    os.system("shutdown /s /t 5")
                elif 'no' in answer:
                    speak('thank you for saving me')
                    break;
                else:
                    speak('please answer in yes or no')

        elif "type what i am saying" in query:
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

Taskexecution()

# run()


       


            



            











