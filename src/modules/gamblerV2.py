import chrome as chrome
import pygetwindow as gw
import discord_bot



with open('token', 'r') as file:
    # Read the contents of the file`r`
    token = file.read()

# run discord bot
client = discord_bot.MyClient()
client.run(token)

