from pickletools import string1
from webbrowser import get
import telebot;
import json
import copy


bot = telebot.TeleBot('5111904045:AAHtJ1_7Am3c9bIq_-YIAqab96c85qqW39U');

global usersList
usersList=[]
global isDay
isDay=False

def initData():
    global usersList
    usersList=[]
    fileObject = open ("data.json",  "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    usersList = json.loads(jsonContent)
    
def printSecretStatus():
    global usersList
    str1=""
    for item in usersList:
        str1+="\n Имя: " + item['name'] + " Статус: " + item['status']
    return str1
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global isDay
    helpStr="Привет, это проект MafiaBot - интеллектуальный Telegram бот ведущего для игру в Мафию. \n Для информации введите /help."
    splitted_text = str(message.text).lower().split()
    if isDay:
        isDay=False
        bot.send_message(message.from_user.id, "Проголосуйте за участников которых надо повесить")
        bot.send_message(message.from_user.id, helpStr)
    elif str(message.text).lower() == "/help":
        str1="MafiaBot - интеллектуальный Telegram бот ведущего для игру в Мафию.. \n Список команд: "\
            "\n /reg \"имя\" - Зарегистрироваться "\
            "\n /status узнать свой статус "\
            "\n /reset - Начать игру заново "\
            "\n /secretStatus - Начать игру заново "\
            "\n Для информации введите /help."
        bot.send_message(message.from_user.id, str1) 
    elif str(message.text).lower() == "/reset":
        isDay=True
        initData()
        bot.send_message(message.from_user.id, "Введите своё имя:")
    else:
        bot.send_message(message.from_user.id, helpStr)


bot.polling(none_stop=True, interval=0)