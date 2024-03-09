import pyautogui as pg


failsafe = pg.PAUSE = 1 




pg.FAILSAFE = False

def pylocker():
    
    pg.click(x=32, y=1054)
    failsafe
    pg.click(x=139, y=988)
    failsafe
    pg.click(x=130, y=914)
    failsafe
    pg.click()


pylocker()


# def pyunlocker():
#     failsafe
#     pg.click(x=139, y=988)
#     # pg.click(x=1271, y=207)
#     failsafe
#     pg.typewrite("",interval=2)

# pyunlocker()
    