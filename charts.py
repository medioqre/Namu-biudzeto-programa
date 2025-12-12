import numpy as np
import matplotlib.pyplot as plt

    
pavadinimas=['Maistas','Transportas','Pramogos']
islaidos=[270, 130, 85]

def bar(pavadinimas, islaidos):

    y=range(len(islaidos))
    plt.bar(y, islaidos, color='green')
    plt.xticks(y, pavadinimas)
    plt.ylabel('I�laidos (EUR)')
    plt.title('I�laidos pagal kategorijas')
    
    plt.show()

def pie(pavadinimas, islaidos):
  
    plt.pie(islaidos, labels=pavadinimas, autopct='%1.1f%%', startangle=140,shadow=True)
    plt.title('I�laidos pagal kategorijas')
    
    plt.show()
