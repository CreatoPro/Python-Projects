from webdriver_manager.microsoft import EdgeChromiumDriver
from selenium import webdriver
import pyautogui as pg


driver_path = (r'F:\Python projects\Shreesat\Class Attender Edge\edgedriver_win64\msedgedriver.exe')
driver = webdriver.Edge(driver_path)
driver.get('https://cuchd.blackboard.com/')
pg.hotkey('win','up')
ok_button = driver.find_element_by_xpath('//*[@id="agree_button"]').click()
username=driver.find_element_by_xpath('//*[@id="loginFormList"]/li[1]/label').click()
pg.typewrite('18bcs6655')
password=driver.find_element_by_xpath('//*[@id="loginFormList"]/li[2]/label').click()
pg.typewrite('@1234Rinku')
login=driver.find_element_by_xpath('//*[@id="entry-login"]').click()
# pg.PAUSE=10
driver.implicitly_wait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content-inner"]/div/header/section/button/bb-svg-icon' ))).click()
# menu=driver.find_element_by_xpath('//*[@id="main-content-inner"]/div/header/section/button/bb-svg-icon"]').click()