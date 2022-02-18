from webbrowser import get
import telebot;
import json
import copy


bot = telebot.TeleBot('5111904045:AAHtJ1_7Am3c9bIq_-YIAqab96c85qqW39U');



global aList
aList=[]
global qList
qList=[]
global isDay
global isNight
global fd
isDay=False
isNight=False
fd=False


def isDayost(minp, maxp):
    global qList
    fList=[]
    for item in qList:
        if int(item ['cost']) >=minp and int(item ['cost']) <=maxp:
            fList.append(item)
    qList=copy.deepcopy(fList)



def initData():
    global aList
    global qList
    fileObject = open ("data.json",  "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    qList=copy.deepcopy(aList)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global isDay
    global isNight
    helpStr="Привет, это проект MafiaBot - интеллектуальный Telegram бот ведущего для игру в Мафию. \n Для информации введите /help."
    splitted_text = str(message.text).lower().split()
    if isDay:
        initData()
        isDayost(int(splitted_text[0]), int(splitted_text[1]))
        isDay=False
        isNight=True
        fd=False
        bot.send_message(message.from_user.id, "Введите минимальное и максимальное количество RAM (в Гб):")
    elif isNight:
        fRam(int(splitted_text[0]), int(splitted_text[1]))
        isDay=False
        isNight=False
        fd=True
        bot.send_message(message.from_user.id, "Введите минимальную и максимальную диагональ (в дюймах):")
    elif str(message.text).lower() == "привет":
        bot.send_message(message.from_user.id, helpStr)
    elif str(message.text).lower() == "/help":
        str1="MafiaBot - интеллектуальный Telegram бот ведущего для игру в Мафию.. \n Список команд: "\
            "\n /s - начать подбор \n Для информации введите /help."
        bot.send_message(message.from_user.id, str1) 
    elif str(message.text).lower() == "/s":
        isDay=True
        isNight=False
        fd=False
        bot.send_message(message.from_user.id, "Введите :")
    else:
        bot.send_message(message.from_user.id, helpStr)


bot.polling(none_stop=True, interval=0)