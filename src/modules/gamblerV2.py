import chrome as chrome
import pygetwindow as gw
import discord_bot


with open('token', 'r') as file:
    # Read the contents of the file
    token = file.read()

# Set chrome to fullscreen
if chrome.checkChromeState() and chrome.isWindowFullscreen(gw.getActiveWindow()) == False:
    chrome.clickFullscreen()

# run discord bot
client = discord_bot.MyClient()
client.run(token)
