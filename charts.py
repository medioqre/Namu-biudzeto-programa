import numpy as np
import matplotlib.pyplot as plt
from data import islaidos_pagal_kategorija, menesio_islaidos

# bar chartas
def bar():
    
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

def pie(pavadinimas, islaidos):
  
    plt.pie(islaidos, labels=pavadinimas, autopct='%1.1f%%', startangle=140,shadow=True)
    plt.title('Išlaidos pagal kategorijas')
    
    plt.show()

# islaidu kas menesi chartas
def menesiai():

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