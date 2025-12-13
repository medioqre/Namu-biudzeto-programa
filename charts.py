import numpy as np
import matplotlib.pyplot as plt
from data import islaidos_pagal_kategorija, menesio_islaidos, menesio_pajamos, menesio_balansas

# bar chartas
def bar():

    paj=menesio_pajamos()
    isl=menesio_islaidos()

    menesiai=[]

    for m in paj.keys():
        if m not in menesiai:
            menesiai.append(m)

    for m in isl.keys():
        if m not in menesiai:
            menesiai.append(m)

    menesiai.sort()

    pajamos = [paj.get(m, 0) for m in menesiai]
    islaidos = [isl.get(m, 0) for m in menesiai]

    x = np.arange(len(menesiai))
    w = 0.4

    plt.bar(x - w/2, pajamos, width=w, label="Pajamos")
    plt.bar(x + w/2, islaidos, width=w, label="Išlaidos")

    plt.xticks(x, menesiai, rotation=45, ha="right")
    plt.xlabel("Mėnuo")
    plt.ylabel("Suma (EUR)")
    plt.title("Pajamos ir išlaidos pagal mėnesį")
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.show()

# pie chartas
def pie():

    data=islaidos_pagal_kategorija()

    pavadinimas=list(data.keys())
    islaidos=list(data.values())
  
    plt.pie(islaidos, labels=pavadinimas, autopct='%1.1f%%', startangle=140,shadow=True)
    plt.title('Išlaidos pagal kategorijas')
    
    plt.show()

# plot menesio balanso chartas
def menesiai():

    bal=menesio_balansas()

    menesiai=list(bal.keys())
    suma=list(bal.values())

    x=np.arange(len(menesiai))
    plt.plot(x,suma,marker='o')

    plt.xticks(x, menesiai, rotation=45, ha='right')
    plt.axhline(0, color='red')
    plt.xlabel('Mėnuo')
    plt.ylabel('Balansas (EUR)')
    plt.title('Mėnesio balansas')
    plt.tight_layout()
    
    plt.show()


bar()
pie()
menesiai()

