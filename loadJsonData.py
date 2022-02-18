import json
import copy

global aList
aList=[]
global qList
qList=[]


def fCost(minp, maxp):
    global qList
    fList=[]
    for item in qList:
        if int(item ['cost']) >=minp and int(item ['cost']) <=maxp:
            fList.append(item)
    qList=copy.deepcopy(fList)
    
def fRam(minp, maxp):
    global qList
    fList=[]
    for item in qList:
        if int(item ['mram']) >=minp*1024 and int(item ['mram']) <= maxp*1024:
            fList.append(item)
    qList=copy.deepcopy(fList)

def fDiag(minp, maxp):
    global qList
    fList=[]
    for item in qList:
        if float(item ['screen diagonal']) >=float(minp) and float(item['screen diagonal']) <= float(maxp):
            fList.append(item)
    qList=copy.deepcopy(fList)

def printJson():
    global qList
    str1=""
    for item in qList:
        # cloth=item['cloth']
        str1+="\n"+"Фирма: " + item['brand'] +" \n Модель: " +item['model']+" \n Цена: "+ item['cost'] + ""\
        "\n Объем RAM: " + item['ram'] + " Диагональ экрана: "  + item['screen diagonal'] + ""\
        "\n Описание: "+ item['description'] + "\n"
    return str1


def initData():
    global aList
    fileObject = open ("data.json",  "r", encoding="UTF-8")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    
if __name__ == '__main__':

    initData()
    qList=copy.deepcopy(aList)
    
    fCost(2000, 40000)
    fRam(0, 6)
    fDiag(2.0, 3.0)
    
    q= printJson()
    print(q)