import pyautogui
from PIL import Image
import pytesseract
import os

os.environ['TESSDATA_PREFIX'] = r'C:/Users/alexa/tesseract/tessdata'  # Update this path as necessary
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/alexa/tesseract/tesseract.exe'

try:
    bet_button = pyautogui.locateOnScreen('src/screenshots/bet.png', confidence=0.9)
except:
    bet_button = None


region = (int(bet_button.left + 181), int(bet_button.top - 46), 56, 36)
screenshot = pyautogui.screenshot(region=region)
screenshot.save("screenshot.png")
screenshot = Image.open("screenshot.png")
text = pytesseract.image_to_string(screenshot)
cleaned_text = text.strip().replace(',', '.')
print(''.join(c for c in cleaned_text if c.isdigit() or c == '.'))