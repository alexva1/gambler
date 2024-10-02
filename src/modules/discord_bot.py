import discord
import re
import bet
from logger import logger
import config
import chrome
import random
import asyncio
import keyboard

async def stayAlive():
    menus = [218, 334, 422, 507, 597]
    random_num = 1
    while True:
        chrome.keepAlive(menus[random_num])
        await asyncio.sleep(random.randint(60,120))
        random_num = get_unique_random(random_num)

async def pause_program():
    print("Program paused. Press 'r' to resume...")
    # Wait asynchronously until the 'r' key is pressed
    await asyncio.to_thread(keyboard.wait, 'r')
    print("Program resumed.")

async def check_for_pause():
    while True:
        # Check if the 'p' key is pressed asynchronously
        if await asyncio.to_thread(keyboard.is_pressed, '`'):
            await pause_program()
        await asyncio.sleep(0.1)  # Small sleep to prevent busy-waiting

async def start_tasks():
    # Run the main task and check_for_pause concurrently
    main_task = asyncio.create_task(stayAlive())
    pause_task = asyncio.create_task(check_for_pause())
    await asyncio.gather(pause_task, main_task)

def get_unique_random(prev_num=None):
    numbers = list(range(5))
    if prev_num is not None:
        numbers.remove(prev_num)
    return random.choice(numbers)

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.processed_urls = set()

    async def on_ready(self):
        print(f'Logged on as {self.user}')
        try:
            # Try to use the existing event loop if one is already running
            loop = asyncio.get_running_loop()
            loop.create_task(start_tasks())
        except RuntimeError:
            # If no event loop is running, start one
            asyncio.run(start_tasks())
    
    async def on_message(self, message):
        # Print the message content and author to the console]
        if message.channel.id == config.CHANNEL_EUROPE or message.channel.id == config.CHANNEL_LIVE or message.channel.id == config.CHANNEL_MAKRO or message.channel.id == config.CHANNEL_NBA or message.channel.id == config.CHANNEL_PRE or message.channel.id == config.CHANNEL_TEST:
            url_pattern = r'https:\/\/www.stoiximan.gr\/mybets\/[^\s]+'
            unit_pattern = r'\d+(?:[.,]\d+)?(?=\s?units?)'
            match = re.search(url_pattern, message.content)
            if match:
                url = match.group(0)
                if url in self.processed_urls:
                    logger.error('Url already processed: ' + url)
                    return
                self.processed_urls.add(url)
                unit_match = re.search(unit_pattern, message.content)
                if unit_match:
                    units = float(unit_match.group().replace(',' , '.'))
                    logger.info('Found url : ' + url + ', Units : ' + str(units))
                    bet.make_bet(url, units)
                else:
                    logger.info('Found url : ' + url + ', Units : Undefined')
                    bet.make_bet(url, config.DEFAULT_UNITS)
                
