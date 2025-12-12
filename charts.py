import numpy as np
import matplotlib.pyplot as plt
from data import islaidos_pagal_kategorija, menesio_islaidos

# bar chartas
def bar(): #-----------padaryk kad bar chartas rodytu pajamas ir islaidas vieno menesio. pvz x asis yra 2025-01 ir y asis bus 2 stulpeliai, vienas rodys pajamas, kitas islaidas
    
    data=islaidos_pagal_kategorija()

    kategorijos=list(data.keys())
    islaidos=list(data.values())

    y=range(len(islaidos))
    plt.bar(y, islaidos, color='green')
    plt.xticks(y, kategorijos)

    plt.xlabel('Išlaidų kategorijos')
    plt.ylabel('Išlaidos (EUR)')
    plt.title('Išlaidos pagal kategorijas')
    
    plt.show()

def pie(pavadinimas, islaidos): #-------padaryk kad rodytu pie pagal islaidu kategorijas 
  
    plt.pie(islaidos, labels=pavadinimas, autopct='%1.1f%%', startangle=140,shadow=True)
    plt.title('Išlaidos pagal kategorijas')
    
    plt.show()

# islaidu kas menesi chartas
def menesiai():#----------pakeisk kad rodytu menesio_balansas() is data.py (dabar rodo menesio_islaidos(), bet butu gerai kad rodytu balansa). ------line plot o ne bar ------

    data=menesio_islaidos() 

    menesiai=list(data.keys())
    suma=list(data.values())

    plt.bar(menesiai, suma, color='orange')
    plt.xlabel('Mėnesiai')
    plt.ylabel('Išlaidos (EUR)')
    plt.title('Išlaidos kiekvieną mėnesį')
    
    plt.show()


bar()
pie()
menesiai()

