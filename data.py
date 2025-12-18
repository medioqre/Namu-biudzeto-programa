from datetime import datetime
import json
from tkinter import messagebox
import os

datafailas = 'data.json'

def load_data():
    if not os.path.exists(datafailas):
        save_data({"pajamos": [], "islaidos": []})
    with open(datafailas, 'r', encoding='utf-8-sig') as f:
        return json.load(f)

def save_data(data):
    with open(datafailas, 'w', encoding='utf-8-sig') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def tikrint_laika(laikas):
    try: 
        datetime.strptime(laikas,"%Y-%m-%d")
        return True
    except:
        messagebox.showerror("Laiko klaida", "Laikas turi būti formatu YYYY-MM-DD")
        return False
        

def add_pajamos(money,kategorija,laikas): 
    data=load_data()
    
    if tikrint_laika(laikas):
        try:
        
            if float(money) <=0:
                messagebox.showerror("Klaida", "Suma turi būti teigiama ir ne nulis")
                return
            data['pajamos'].append({
            'money':float(money), 
            'paj_kategorija':kategorija,
            'laikas':laikas})
            save_data(data)
            return True
        except ValueError:
            messagebox.showerror("Pajamų error","Nepalikite sumos lauko tuščio ir neįrašykite raidžių")
            return False
   
def add_islaidos(money,kategorija,laikas,pavadinimas):
    data=load_data()
    
    try:
        tikrint_laika(laikas)
        if float(money) <=0:
            messagebox.showerror("Klaida", "Suma turi būti teigiama ir ne nulis")
            return
        data['islaidos'].append({
        'money':float(money), 
        'isl_kategorija':kategorija,
        'laikas':laikas,
        'pavadinimas':pavadinimas,})
        save_data(data)
        return True
    except ValueError:
        messagebox.showerror("Išlaidų error","Nepalikite sumos lauko tuščio ir neįrašykite raidžių") 
        return False
    
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
    return kategoriju_sumos

def menesio_pajamos():
    data=load_data()
    menesio_paj_suma={}

    for i in data['pajamos']:
        laikas=i["laikas"] 
        menesis=laikas[:7] 
        islaidos=i['money'] 
        menesio_paj_suma[menesis] = menesio_paj_suma.get(menesis,0)+islaidos 
    return menesio_paj_suma

def menesio_islaidos():
    data=load_data()
    menesio_isl_suma={}

    for i in data['islaidos']:
        laikas=i["laikas"] 
        menesis=laikas[:7] 
        islaidos=i['money'] 
        menesio_isl_suma[menesis] = menesio_isl_suma.get(menesis,0)+islaidos 
    return menesio_isl_suma

def pajamu_sar():
    duomenys=load_data()
    return duomenys.get('pajamos',[])

def islaidu_sar():
    duomenys=load_data()
    return duomenys.get('islaidos',[])

def menesio_balansas():
    paj= menesio_pajamos()
    isl= menesio_islaidos()
    balansas={}
    for menesis in paj:
        balansas[menesis] = paj.get(menesis,0) -isl.get(menesis,0)

    for menesis in isl:
        if menesis not in balansas:
            balansas[menesis] = paj.get(menesis,0) - isl.get(menesis, 0)
    return dict(sorted(balansas.items()))

def gaut_menesius():
    data = load_data()
    menesiai = set()

    for i in data.get("pajamos", []):
        menesiai.add(i["laikas"][:7])

    for i in data.get("islaidos", []):
        menesiai.add(i["laikas"][:7])

    return sorted(menesiai)

def total_balansas():
    menesiubalansai=sum(list(menesio_balansas().values()))
    return menesiubalansai