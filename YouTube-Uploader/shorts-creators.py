# import time
# from selenium import webdriver 
# from selenium.webdriver.chrome.options import Options
# import webbrowser
# import os
# import pyautogui

# chrome_path = r'C:\ Program Files (x86)\ Google\ Chrome\ Application\ chrome.exe %s'


# webbrowser.get(chrome_path)
# webbrowser.open_new_tab("https://studio.youtube.com/")
# time.sleep(10)
# create = pyautogui.locateCenterOnScreen('create.png')#If the file is not a png file it will not work
# print(create)
# pyautogui.moveTo(create)
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
# upload = pyautogui.locateCenterOnScreen('upload.png')
# print(upload)
# pyautogui.moveTo(upload)
# time.sleep(2)
# pyautogui.click()
# time.sleep(2)
# select = pyautogui.locateCenterOnScreen('select.png')
# print(select)
# pyautogui.moveTo(select)
# time.sleep(2)
# pyautogui.click()

# current_folder = os.getcwd()
# print("Current folder:", current_folder)

# time.sleep(2)
# file_name = pyautogui.locateCenterOnScreen('file_name.png')
# print(file_name)
# pyautogui.moveTo(file_name)
# time.sleep(2)
# pyautogui.click()



from pytube import YouTube

# Replace 'VIDEO_URL' with the URL of the age-restricted video
video_url = 'https://www.youtube.com/watch?v=Vqa7wLcQr38'


yt = YouTube(video_url)
yt.streams.first().download()