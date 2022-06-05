import asyncio
import os
from pyrogram import Client
from config import *
logins_list = []
apps = []
from_sleep, to_sleep = 7200, 10800


for root, dirs, files in os.walk("./"):
    for file in files:
        if(file.endswith(".session")):    
            logins_list.append(file.split(".")[0])

async def main():
    for login in logins_list:
        apps.append(Client(login, api_id, api_hash))
       
    for app in apps:
        await app.start()
        try:
            await app.join_chat(channel1_link.split("https://t.me/")[1])
            await app.join_chat(channel2_link.split("https://t.me/")[1])
        except:
            try:
                await app.join_chat(channel1_link.split("https://t.me/")[1])
            except: pass
        
        print("Ok ")
    for app in apps:
        await app.stop()

asyncio.run(main())

