import pyautogui
import pygetwindow as gw
from logger import logger
import config
import time
import bet
import pytesseract
from PIL import Image
import os

os.environ['TESSDATA_PREFIX'] = r'C:/Users/alexa/tesseract/tessdata'  # Update this path as necessary
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/alexa/tesseract/tesseract.exe'


def clickSearchBar():
    pyautogui.click(923,78)
    logger.info('Search bar clicked.')

def typeUrl(url: str):
    pyautogui.typewrite(url)
    pyautogui.press('enter')
    logger.info('Url typed in the search bar.')


def valueSetter(value: float):
    counter = 0
    if value >= config.MAX_UNITS:
        value = config.DEFAULT_UNITS

    if value < config.MAX_UNITS:
        while counter < 100:
            counter += 1
            try:
                bet_button_location = pyautogui.locateOnScreen('src/screenshots/bet_button_grey.png', confidence=0.9)
            except:
                bet_button_location = None
                pass

            if bet_button_location is not None:
                try:
                    value_location = pyautogui.locateOnScreen('src/screenshots/value.png', confidence=0.9)
                except:
                    value_location = None
                    pass

                if value_location is not None:
                    # Get the center of the located image
                    image_center = pyautogui.center(value_location)
                    pyautogui.click(image_center)
                    pyautogui.typewrite(str(round(value*config.UNIT_VALUE, 2)))
                    logger.info('Value is set to ' + str(round(value*config.UNIT_VALUE, 2)))
                    break
                else:
                    logger.error('Bet is locked before setting value.')
                    valueSetter(value)
                    return
                    
            else: 
                pyautogui.scroll(-30) 
        if counter >= 100:   
            logger.error('Value set area could\'t be located.')
    else:
        logger.critical('Bet value is greater than the max value allowed.')    

def betPlacer():
    counter = 0
    while counter < 100: 
        try:
            bet_button_location = pyautogui.locateOnScreen('src/screenshots/bet.png', confidence=0.9)
        except:
            bet_button_location = None
            pass    
        
        if bet_button_location is not None:
            image_center = pyautogui.center(bet_button_location)
            pyautogui.click(image_center)
            logger.info('Tried clicking bet button.')
            time.sleep(3)
            logger.info('Bet is successfully placed.')
            return
        time.sleep(0.1)


    logger.error('Bet is locked.')
    return
        


def loadCheck() -> bool:
    try:
        deltio_location = pyautogui.locateOnScreen('src/screenshots/load_check.png')
    except:
        deltio_location = None
        pass

    if deltio_location is not None:
        return True
    else:
        return False
    
def clickNewTab():
    pyautogui.click(366,25)
    logger.info('New tab is opened.')

def clickDeleteTab():
    pyautogui.middleClick(488,23)
    logger.info('Tab is closed.')


def keepAlive(menu):
    pyautogui.click(menu,191)
    
