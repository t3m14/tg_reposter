#Импортируем необходимые библиотеки
import asyncio
import os
from pyrogram import Client, idle, filters
from random import randint, choices
from config import *
#Служебные глобальные переменные
i = 0
logins_list = []
apps = []
accounts_to_use = ""
#Начинаем работу с составления списка сессий
print("GETTING SESSIONS...")
for root, dirs, files in os.walk("./"):
    for file in files:
        if(file.endswith(".session")):    
            logins_list.append(file.split(".")[0])
         
print("STARTING...")
async def main():
    global accounts_to_use
    accounts_to_use = round(len(logins_list)/100 * (50 - randint(1, 49)))
    
    #Заполняем список приложений на основе списка сессий
    for login in logins_list:
        apps.append(Client(login, api_id, api_hash))
    
    for app in apps: #Асинхронно запускаем приложения по порядку
        print("SESSION OK")
        await app.start()
        
    
        #Хэндлер который видит пост на первом канале, когда он выходит
        @app.on_message(filters.channel(channel1_link, "m"))
        async def get_post_and_put_to_queue(client, message):
            print("POST GETTED" + str(message.id))
            #Создаём очередь для обработки постов, на каждый аккаунт приходится несколько постов
            await asyncio.create_task(channel_handler(message, queue))
            
        #Хэндлер который видит пост на втором канале, когда он выходит    
        @app.on_message(filters.channel(channel2_link, "m"))
        async def get_post_and_put_to_queue(client, message):
            print("POST GETTED" + str(message.id))
            #Создаём такую же очередь для постов другого канала
            await asyncio.create_task(channel_handler(message, queue))
            
        #Асинхронная функция обработки поста
        async def channel_handler(message, queue):
            try:  
                global i
                global accounts_to_use
                
                if message.entities or message.caption_entities :
                    pass
                else:
                    i += 1
                    if i >= len(logins_list):
                        i = 0
                        accounts_to_use = round(len(logins_list)/100 * (50 - randint(1, 49)))
                    elif i <= accounts_to_use:
                        return
                    
                    #Рандомная задержка между репостами для одного аккаунта
                    await asyncio.sleep(randint(from_sleep, to_sleep))
                    #Пересылаем сообщение в личку
                    await message.forward(username_to_send)
                    print("POST FORWARDED")
                    #Заканчиваем задачу, чтобы освободить очередь
            except: pass    
    
    #Ожидание приложения до следующего сигнала
    await idle()
    #Закрываем все приложения, когда программа будет закрыта
    for app in apps:
        await app.stop()

#Начинаем здесь
if __name__ == "__main__": 
    print("STARTED SUCCESSFULL")
    queue = asyncio.Queue() #Инициализируем очередь для глобального использования
    asyncio.run(main()) #Запускаем асинхронно основную функцию
    

