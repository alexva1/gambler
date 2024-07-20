import pyautogui
import pygetwindow as gw
from logger import logger
import config


def checkChromeState() -> bool:
    """
    Checks if chrome is focused

    Return:
        True if chrome browser is focused.
    """

    # Get focused window
    focused_window = gw.getActiveWindow()

    if focused_window is not None:
        
        # If title contains Google Chrome return True
        if 'Google Chrome' in focused_window.title:
            return True
        
    # Else return False
    return False

def isWindowFullscreen(window: (gw.Win32Window | None)) -> bool:
    """
    Checks if a window is on fullscreen

    Args:
        window: Win32Window | None
            A window

    Return:
        True if window provided is on fullscreen.
    """

    # If window provided is None then throw exception
    if window == None:
        raise ValueError('The window provided is Null.')

    # Get position of window
    window_left, window_top, window_right, window_bottom = window.left, window.top, window.right, window.bottom
    
    
    # If window covers the entire screen return true
    if (window_left == -9 and window_top == -9 and 
        window_right == 1929 and window_bottom == 1029):
        return True
    
    # Else return False
    return False

def clickFullscreen():

    try:
        button_location = pyautogui.locateOnScreen('src/screenshots/fullscreen_button.png', confidence=0.9)
    except:
        button_location = None
        pass

    if button_location is not None:
        # Get the center of the located image
        image_center = pyautogui.center(button_location)
        pyautogui.click(image_center)
    
    return

def clickSearchBar():
    if checkChromeState():
        pyautogui.click(923,78)
        logger.info('Search bar clicked.')

def typeUrl(url: str):
    if checkChromeState():
        pyautogui.typewrite(url)
        pyautogui.press('enter')
        logger.info('Url typed in the search bar.')


def valueSetter(value: float):
    counter = 0
    if value < config.MAX_VALUE:
        while counter < 100:
            counter += 1
            try:
                bet_button_location = pyautogui.locateOnScreen('src/screenshots/bet.png', confidence=0.9)
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
                    pass
            else: 
                pyautogui.scroll(-30) 
        if counter >= 100:   
            logger.error('Value set area could\'t be located.')
    else:
        logger.critical('Bet value is greater than the max value allowed.')    

def betPlacer():
    try:
        bet_button_location = pyautogui.locateOnScreen('src/screenshots/bet.png', confidence=0.9)
    except:
        bet_button_location = None
        pass

    if bet_button_location is not None:
        image_center = pyautogui.center(bet_button_location)
        pyautogui.click(image_center)
        logger.info('Bet is successfully placed.')
    else:
        logger.error('Could\'t find the bet button.')

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