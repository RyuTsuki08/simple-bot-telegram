#https://api.telegram.org/

#https://core.telegram.org/bots/api

#imports librarys

import requests

#variables
token = "yourtoken"

#code

for x in range(0, 3):
    if x == 0:
        x = requests.post('https://api.telegram.org/bot<yourtoken>/sendPhoto', 
        files = {'photo': ('python/bot_1/felij.jpg', open('python/bot_1/felij.jpg', 'rb'))} , data = {'chat_id': '@probandoBotjiji', 'caption' : 'felij :)'})
    if x == 1:
        x = requests.post('https://api.telegram.org/bot<yourtoken>/sendPhoto', 
        files = {'photo': ('python/bot_1/truste.jpg', open('python/bot_1/truste.jpg', 'rb'))} , data = {'chat_id': '@probandoBotjiji', 'caption' : 'truste :('})
    if x == 2:
        x = requests.post('https://api.telegram.org/bot<yourtoken>/sendPhoto', 
        files = {'photo': ('python/bot_1/descarga.jpg', open('python/bot_1/descarga.jpg', 'rb'))} , data = {'chat_id': '@probandoBotjiji', 'caption' : 'enojao >:('})
