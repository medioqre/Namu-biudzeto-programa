from datetime import datetime
import json
from tkinter import messagebox
import os

datafailas = 'data.json'

isl_kategorijos=['Maistas','Transportas','Laisvalaikis ir pramogos','Kitos išlaidos']
paj_kategorijos=['Darbas', 'Dovanos','Kitos pajamos'] #nzn kazkas kitas pridekit daugiau
def load_data():
    with open(datafailas, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def save_data(data):
    with open(datafailas, 'w', encoding='utf-8-sig') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def tikrint_laika(laikas):
    try: 
        datetime.strptime(laikas,"%Y-%m-%d")
        return False
    except ValueError:
        return True 

def add_pajamos(money,kategorija,laikas,Tree): 
    data=load_data()
    if tikrint_laika(laikas):
        messagebox.showerror("Laiko klaida", "Laikas turi būti formatu YYYY-MM-DD ir būti teisinga")
    else:
        try:
            data['pajamos'].append({
            'money':float(money), 
            'paj_kategorija':kategorija,
            'laikas':laikas})
            save_data(data)
            Tree.insert('','end',values=(laikas,kategorija,money))
        except ValueError:
            messagebox.showerror("Pajamų error","Nepalikite sumos lauko tuščio ir neįrašykite raidžių")
   
def add_islaidos(money,kategorija,laikas,pavadinimas):
    data=load_data()
    if tikrint_laika(laikas):
        messagebox.showerror("Laiko klaida", "Laikas turi būti formatu YYYY-MM-DD ir būti teisinga")
    else:
        try:
            data['islaidos'].append({
            'money':float(money), 
            'isl_kategorija':kategorija,
            'laikas':laikas,
            'pavadinimas':pavadinimas,})
            save_data(data)
        except ValueError:
            messagebox.showerror("Išlaidų error","Nepalikite sumos lauko tuščio ir neįrašykite raidžių") 
    
def delete_pajama(money,kategorija,laikas):
    data=load_data()
    for i in data['pajamos']:
        if i['money'] == float(money) and i['paj_kategorija'] == kategorija and i['laikas'] == laikas:
            data['pajamos'].remove(i)
            break
    save_data(data)

def delete_islaida(pavadinimas, money,kategorija,laikas):
    data=load_data()
    for i in data['islaidos']:
        if i['pavadinimas'] == pavadinimas and i['money'] == float(money) and i['isl_kategorija'] == kategorija and i['laikas'] == laikas:
            data['islaidos'].remove(i)
            break
    save_data(data)

def islaidos_pagal_kategorija():
    data=load_data()
    kategoriju_sumos={}
    for i in data["islaidos"]:
        if i['isl_kategorija'] not in kategoriju_sumos:
            kategoriju_sumos[i['isl_kategorija']] = 0

        kategoriju_sumos[i['isl_kategorija']] += i['money']
    print(kategoriju_sumos)
    return kategoriju_sumos

def menesio_pajamos():
    data=load_data()
    menesio_paj_suma={}

    for i in data['pajamos']:
        laikas=i["laikas"] #duoda pvz '2025-10-20'
        menesis=laikas[:7] # palieka tik '2025-10'
        islaidos=i['money'] #duoda tos dienos islaidos eur
        menesio_paj_suma[menesis] = menesio_paj_suma.get(menesis,0)+islaidos #.get sako -> jei menesio_suma[menesis] egzistuoja, tai naudoti jo reiksme, o jeigu ne tai naudoti 0. pvz menesis='2025-05' ir kolkas nera jo menesio_suma={} zodyne, tai bus menesio_suma['2025-05']=0+islaidos

    print(menesio_paj_suma)
    return menesio_paj_suma


def menesio_islaidos():
    data=load_data()
    menesio_isl_suma={}

    for i in data['islaidos']:
        laikas=i["laikas"] #duoda pvz '2025-10-20'
        menesis=laikas[:7] # palieka tik '2025-10'
        islaidos=i['money'] #duoda tos dienos islaidos eur
        menesio_isl_suma[menesis] = menesio_isl_suma.get(menesis,0)+islaidos #.get sako -> jei menesio_suma[menesis] egzistuoja, tai naudoti jo reiksme, o jeigu ne tai naudoti 0. pvz menesis='2025-05' ir kolkas nera jo menesio_suma={} zodyne, tai bus menesio_suma['2025-05']=0+islaidos

    print(menesio_isl_suma)
    return menesio_isl_suma

def pajamu_sar():
    duomenys=load_data()
    return duomenys.get('pajamos',[])

def islaidu_sar():
    duomenys=load_data()
    islaidos=duomenys.get('islaidos',[])

menesio_islaidos()
menesio_pajamos()

"""
#-------------temporary to see what data.py functions do-----------
data=load_data() # cia dabar dictionary
print(data) 
print(f'\n{data["pajamos"][0]['money']}') #printina "900" 
print(f'\n{data["pajamos"][0]['paj_kategorija']}') #printina is kur gavo tuos pinigus (pajamu kategorija)
print(f'\n{data["pajamos"][0]['laikas']}') #printina kada gauti pinigai 
#jei bandysime vietoj [0] parasyti [1] bus error nes tik vienas pajamos entry yra 
save_data(data) #saving data i json file


print(f'\n{data["islaidos"][0]['pavadinimas']}') #printina islaidu pavadinima
print(f'\n{data["islaidos"][0]['money']}') #printina kada gauti pinigai 
print(f'\n{data["islaidos"][0]['laikas']}') #printina laikas
print(f'\n{data["islaidos"][0]['isl_kategorija']}') #printina islaidu kategorija
"""