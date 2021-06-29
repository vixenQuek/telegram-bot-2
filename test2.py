
import time 
from typing import Text
from telethon import TelegramClient, events #,Button
from telethon.tl.custom import Button
from datetime import timedelta
import logging
import asyncio
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

from telethon.tl.types import InputPeerChannel
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                   level=logging.INFO)



# client telegram api
api_id = 4407795
api_hash = '7774cfea690ea5ba39ed1b15c9a5f0f6'


# InputPeerChannel(channel_id=, access_hash=)


INPUT1 = 1168502525
token = '1840281216:AAFzyYbybV2UtLcjclgV0a2jGvzPS9yTB0E'

client2 = TelegramClient("bot5", api_id, api_hash).start(bot_token=token)
def main():
    client2.start()
    print("Userbot on!")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(auto_message())
    client2.run_until_disconnected()


async def auto_message():



    while True:
        keyboard = [
        [  
        Button.inline("play", b"1"), 
        Button.inline("score", b"2"),
        Button.inline("reward", b"3"), 
        Button.inline("FAQ", b"4")
        ],
        [
        Button.inline("Hall of Fame", b"5")
        ]
        ]
        # ch = await client2.get_entity(InputPeerChannel(channel_id=1437949857, access_hash=-752516512759929280))
        # print(ch)

        await client2.send_message(entity=INPUT1, message='''VAPERS PLAY NOW!

Click on one of the buttons below to start playing for rewards

Play: Start Game

Score: Check Current Scoreboard

Rewards: View Prizes

FAQ: Frequently Asked Questions

Hall Of Fame: Display Winners''', buttons=keyboard)
        time.sleep(180)




if __name__ == '__main__':
    main()


