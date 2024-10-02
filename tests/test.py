import time
import pyautogui

confidence_level = 0.9

time.sleep(2)

try:
    deltio_location = pyautogui.locateOnScreen('src/screenshots/load_check.png', confidence=confidence_level)
    
except:
    deltio_location = None

try:
    bet_button_grey = pyautogui.locateOnScreen('src/screenshots/bet_button_grey.png', confidence=confidence_level)
except:
    bet_button_grey = None

try:
    bet_button = pyautogui.locateOnScreen('src/screenshots/bet.png', confidence=confidence_level)
except:
    bet_button = None

try:   
    value_button = pyautogui.locateOnScreen('src/screenshots/value.png', confidence=confidence_level)
except:
    value_button = None
   
if deltio_location is not None:
    print('Object deltio was found! ')
else:
    print('Object deltio was not found!')

if bet_button_grey is not None:
    print('Object bet button grey was found! ')
else:
    print('Object bet button grey was not found!')    

if bet_button is not None:
    print('Object bet button was found! ')
else:
    print('Object bet button was not found!')

if value_button is not None:
    print('Object value button was found! ')
else:
    print('Object value button was not found!')    