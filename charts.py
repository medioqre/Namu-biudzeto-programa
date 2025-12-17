import numpy as np
import matplotlib.pyplot as plt
from data import islaidos_pagal_kategorija, menesio_islaidos, menesio_pajamos, menesio_balansas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# bar chartas
def bar(parent):

    for widget in parent.winfo_children():
        widget.destroy()

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

    fig=Figure(figsize=(6,4))
    ax=fig.add_subplot(111)

    x = np.arange(len(menesiai))
    w = 0.4

    ax.bar(x - w/2, pajamos, width=w, label="Pajamos")
    ax.bar(x + w/2, islaidos, width=w, label="Išlaidos")

    ax.set_xticks(x)
    ax.set_xticklabels(menesiai, rotation=45, ha='right')
    ax.set_xlabel('Mėnuo')
    ax.set_ylabel('Pajamos ir išlaidos (EUR)')
    ax.set_title('Mėnesio pajamos ir išlaidos')
    fig.tight_layout()
    ax.legend()
    


    canvas=FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both',expand=True)

# pie chartas
def pie(parent):

    for widget in parent.winfo_children():
        widget.destroy()

    data=islaidos_pagal_kategorija()

    pavadinimas=list(data.keys())
    islaidos=list(data.values())

    fig=Figure(figsize=(6,4))
    ax=fig.add_subplot(111)
  
    ax.pie(islaidos, labels=pavadinimas, autopct='%1.1f%%', startangle=140,shadow=True)
    ax.set_title('Išlaidos pagal kategorijas')

    canvas=FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both',expand=True)
    

# plot menesio balanso chartas
def menesiai(parent):

    for widget in parent.winfo_children():
        widget.destroy()

    bal=menesio_balansas()

    menesiai=list(bal.keys())
    suma=list(bal.values())

    fig=Figure(figsize=(6,4))
    ax=fig.add_subplot(111)

    x=np.arange(len(menesiai))
    ax.plot(x,suma,marker='o')

    ax.set_xticks(x)
    ax.set_xticklabels(menesiai, rotation=45, ha='right')
    ax.axhline(0, color='red')
    ax.set_xlabel('Mėnuo')
    ax.set_ylabel('Balansas (EUR)')
    ax.set_title('Mėnesio balansas')
    fig.tight_layout()

    canvas=FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both',expand=True)

