import json
datafailas = 'data.json'

kategorijos=['Maistas','Transportas','Laisvalaikis ir pramogos','Kitos išlaidos']

def load_data():
    with open(datafailas, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def save_data(data):
    with open(datafailas, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_pajamos(): #+ pajamos,kategorija iskaiciuotinai
    pajamusuma=[i['money'] for i in data['pajamos']]
    paj_kategorija=[i['paj_kategorija'] for i in data['pajamos']]

def add_islaidos(islaidos,kategorija, daiktopavadinimas, menesis):
    pass

def islaidos_pagal_kategorija():
    pass

def menesiototal():
    pass



data=load_data()
print(add_pajamos()) # duoda list kuris rodo [900] ir tik vienas dalykas nes tik vienas ir yra smh


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