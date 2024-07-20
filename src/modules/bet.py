import chrome as chrome
import time
import pyautogui

def make_bet(url: str, units: float):
    chrome.clickNewTab()
    chrome.clickSearchBar()
    chrome.typeUrl(url)
    while chrome.loadCheck() == False:
        time.sleep(0.2)
    pyautogui.moveTo(959, 687)
    chrome.valueSetter(units)
    time.sleep(1)
    chrome.betPlacer()
    time.sleep(10)
    chrome.clickDeleteTab()