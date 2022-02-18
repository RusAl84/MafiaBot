from webbrowser import get
import telebot;
import json
import copy


bot = telebot.TeleBot('5111904045:AAHtJ1_7Am3c9bIq_-YIAqab96c85qqW39U');

global usersList
usersList=[]
global isDay
isDay=True

def initData():
    global usersList
    usersList=[]
    # fileObject = open ("data.json",  "r", encoding="UTF-8")
    # jsonContent = fileObject.read()
    # aList = json.loads(jsonContent)
    # qList=copy.deepcopy(aList)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global isDay
    helpStr="Привет, это проект MafiaBot - интеллектуальный Telegram бот ведущего для игру в Мафию. \n Для информации введите /help."
    splitted_text = str(message.text).lower().split()
    if isDay:

        isDay=False

        fd=False
        bot.send_message(message.from_user.id, "Введите :")
    elif isNight:

        isDay=False
        isNight=False
        fd=True
        bot.send_message(message.from_user.id, "Введите :")
    elif str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, helpStr)
    elif str(message.text).lower() == "/help":
        str1="MafiaBot - интеллектуальный Telegram бот ведущего для игру в Мафию.. \n Список команд: "\
            "\n /reg - Зарегистрироваться "\
            "\n /reset - Начать игру заново "\
            "\n Для информации введите /help."
        bot.send_message(message.from_user.id, str1) 
    elif str(message.text).lower() == "/re":
        isDay=True
        isNight=False
        fd=False
        bot.send_message(message.from_user.id, "Введите имя:")
    else:
        bot.send_message(message.from_user.id, helpStr)


bot.polling(none_stop=True, interval=0)