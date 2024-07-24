import discord
import re
import bet
from logger import logger
import config
import chrome
import time
import random


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        while True:
            chrome.keepAlive()
            time.sleep(random.randint(300,600))
    
    async def on_message(self, message):
        # Print the message content and author to the console
        if message.channel.id == config.CHANNEL_EUROPE or message.channel.id == config.CHANNEL_LIVE or message.channel.id == config.CHANNEL_MAKRO or message.channel.id == config.CHANNEL_NBA or message.channel.id == config.CHANNEL_PRE:
            url_pattern = r'https:\/\/www.stoiximan.gr\/mybets\/[^\s]+'
            unit_pattern = r'(\d+(\.\d+)?)\s*unit(s)?'
            match = re.search(url_pattern, message.content)
            if match:
                url = match.group(0)
                unit_match = re.search(unit_pattern, message.content)
                if unit_match:
                    units = float(unit_match.group(1))
                    logger.info('Found url : ' + url + ', Units : ' + str(units))
                    bet.make_bet(url, units)
                else:
                    logger.info('Found url : ' + url + ', Units : Undefined')
                    bet.make_bet(url, config.DEFAULT_UNITS)
                
