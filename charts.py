import numpy as np
import matplotlib.pyplot as plt

# bar chartas
def bar():

    kategorija=['Maistas','Transportas','Pramogos']
    islaidos=[270, 130, 85]

    y=range(len(islaidos))
    plt.bar(y, islaidos, color='green')
    plt.xticks(y, kategorija)
    plt.xlabel('Išlaidų kategorijos')
    plt.ylabel('Išlaidos (EUR)')
    plt.title('Išlaidos pagal kategorijas')
    
    plt.show()

# pie chartas
def pie():

    kategorija=['Maistas','Transportas','Pramogos']
    islaidos=[270, 130, 85]
  
    plt.pie(islaidos, labels=kategorija, autopct='%1.1f%%', startangle=140,shadow=True)
    plt.title('Išlaidos pagal kategorijas')
    
    plt.show()

# islaidu kas menesi chartas
def menesiai():

    menesiai=['Sausis','Vasaris','Kovas','Balandis','Gegužė']
    islaidu_suma=[500, 600, 550, 700, 650]

    plt.bar(menesiai, islaidu_suma, color='orange')
    plt.xlabel('Mėnesiai')
    plt.ylabel('Išlaidos (EUR)')
    plt.title('Išlaidos kiekvieną mėnesį')
    
    plt.show()

# aisku duomenys random kaip pvz. paiimti

bar()
pie()
menesiai()