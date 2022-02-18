import json
ListOfItems=[]
item1={}
item1['brand']="Samsung"
item1['model']="Galaxy S21 FE 5G"
item1['cost']="54 990"
ListOfItems.append(item1)
item2={}
item2['brand']="Samsung"
item2['model']="Galaxy Z Flip3 5G"
item2['cost']="84 990"
ListOfItems.append(item2)
item3={}
item3['brand']="Samsung"
item3['model']="Galaxy Z Fold3 5G"
item3['cost']="144 990"
ListOfItems.append(item3)
item4={}
item4['brand']="Samsung"
item4['model']="Galaxy A32"
item4['cost']="19 990"
ListOfItems.append(item4)
item5={}
item5['brand']="Samsung"
item5['model']="Galaxy S20 FE"
item5['cost']="47 990"
ListOfItems.append(item5)
item6={}
item6['brand']="Samsung"
item6['model']="Galaxy A52"
item6['cost']="26 990"
ListOfItems.append(item6)
item7={}
item7['brand']="Samsung"
item7['model']="Galaxy A22s 5G"
item7['cost']="19 990"
ListOfItems.append(item7)
item8={}
item8['brand']="Apple"
item8['model']="iPhone 13"
item8['cost']="74 460"
ListOfItems.append(item8)
item9={}
item9['brand']="Apple"
item9['model']="iPhone 11"
item9['cost']="52 620"
ListOfItems.append(item9)
item10={}
item10['brand']="Apple"
item10['model']="iPhone 12"
item10['cost']="65 500"
ListOfItems.append(item10)
item11={}
item11['brand']="Apple"
item11['model']="iPhone SE"
item11['cost']="38 990"
ListOfItems.append(item11)
item12={}
item12['brand']="Apple"
item12['model']="iPhone XS MAX"
item12['cost']="59 490"
ListOfItems.append(item12)
item13={}
item13['brand']="XIAOMI"
item13['model']="MI 11 ULTRA"
item13['cost']="79 900"
ListOfItems.append(item13)
item14={}
item14['brand']="XIAOMI"
item14['model']="MI 11 PRO"
item14['cost']="55 790"
ListOfItems.append(item14)
item15={}
item15['brand']="XIAOMI"
item15['model']="MI 11 LITE"
item15['cost']="27 899"
ListOfItems.append(item15)
item16={}
item16['brand']="XIAOMI"
item16['model']="MI 10S"
item16['cost']="25 399"
ListOfItems.append(item16)
item17={}
item17['brand']="XIAOMI"
item17['model']="MI 10 ULTRA"
item17['cost']="27 899"
ListOfItems.append(item17)
item18={}
item18['brand']="XIAOMI"
item18['model']="MI 9 PRO"
item18['cost']="41 990"
ListOfItems.append(item18)
item19={}
item19['brand']="XIAOMI"
item19['model']="MI 9 LITE"
item19['cost']="25 399"
ListOfItems.append(item19)
item20={}
item20['brand']="Nokia"
item20['model']="Nokia 3310"
item20['cost']="2 285"
ListOfItems.append(item20)
item21={}
item21['brand']="ASUS"
item21['model']="ROG Phone"
item21['cost']="83 010"
ListOfItems.append(item21)
item22={}
item22['brand']="Oppo"
item22['model']="A55"
item22['cost']="15 990"
ListOfItems.append(item22)


jsonString = json.dumps(ListOfItems,ensure_ascii=False, indent=4, sort_keys=True)
jsonFile = open("data.json", "w", encoding="UTF-8")
jsonFile.write(jsonString)
jsonFile.close()