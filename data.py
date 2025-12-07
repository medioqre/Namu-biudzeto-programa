import json
datafailas = 'data.json'

kategorijos=['Maistas','Transportas','Laisvalaikis ir pramogos','Kitos išlaidos']

def load_data():
    with open(datafailas, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def save_data(data):
    with open(datafailas, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_pajamos(money,kategorija,laikas): 
    data=load_data()
    data['pajamos'].append({
        'money':money,
        'paj_kategorija':kategorija,
        'laikas':laikas})
    save_data(data)

def add_islaidos(money,kategorija,laikas,pavadinimas):
    data=load_data()
    data['islaidos'].append({
        'money':money,
        'isl_kategorija':kategorija,
        'laikas':laikas,
        'pavadinimas':pavadinimas,
        })
    save_data(data)

def islaidos_pagal_kategorija():
    data=load_data()
    kategorija=add_islaidos()[0]
    islaidos_suma=add_islaidos()[1]
    kategoriju_sumos={}
    for kateg, islaidos in zip(kategorija,islaidos_suma): #zip susieja 2 list pvz [1,2,3] ir antras list ['a','b','c'], tai zip(pirmaslist,antraslist) output padaro 1 a, 2 b, 3 c  (ne kableliais o nauja line)
        if kateg not in kategoriju_sumos:
            kategoriju_sumos[kateg]=0
        kategoriju_sumos[kateg]+=islaidos
    return kategoriju_sumos
    #print(kategorijos_suma)

def menesio_total():
    data=load_data()
    menesio_suma={}

    for i in data['islaidos']:
        laikas=i["laikas"] #duoda pvz '2025-10-20'
        menesis=laikas[:7] # palieka tik '2025-10'
        islaidos=i['money'] #duoda tos dienos islaidos eur
        menesio_suma[menesis] = menesio_suma.get(menesis,0)+islaidos #.get sako -> jei menesio_suma[menesis] egzistuoja, tai naudoti jo reiksme, o jeigu ne tai naudoti 0. pvz menesis='2025-05' ir kolkas nera jo menesio_suma={} zodyne, tai bus menesio_suma['2025-05']=0+islaidos

    #print(menesio_suma)
    return menesio_suma




#add_islaidos() # duoda kelis list is data.json 

"""
#-------------temporary to see what data.py functions do-----------
data=load_data() # cia dabar dictionary
print(data) 
print(f'\n{data["pajamos"][0]['money']}') #printina "900" 
print(f'\n{data["pajamos"][0]['paj_kategorija']}') #printina is kur gavo tuos pinigus (pajamu kategorija)
print(f'\n{data["pajamos"][0]['laikas']}') #printina kada gauti pinigai 
#jei bandysime vietoj [0] parasyti [1] bus error nes tik vienas pajamos entry yra 
save_data(data) #saving data i json file


print(f'\n{data["islaidos"][0]['pavadinimas']}') #printina kada gauti pinigai 
print(f'\n{data["islaidos"][0]['money']}') #printina kada gauti pinigai 
print(f'\n{data["islaidos"][0]['laikas']}') #printina kada gauti pinigai 
print(f'\n{data["islaidos"][0]['isl_kategorija']}') #printina kada gauti pinigai 
"""