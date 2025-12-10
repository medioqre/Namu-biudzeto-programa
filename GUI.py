from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from data import add_pajamos, pajamu_sar, islaidu_sar, delete_pajama

def GUI():

    #Pagrindinis langas
    Pagrindinis_langas=Tk()
    Pagrindinis_langas.title('Namų biudžeto skaičiuoklė')
    Pagrindinis_langas.geometry('800x500')

    #Main meniu------------------------------------------
    Meniu=Menu(Pagrindinis_langas)
    Pagrindinis_langas.config(menu=Meniu)
    Main_meniu=Menu(Meniu)
    Meniu.add_cascade(label='Menu', menu=Main_meniu)

    Main_meniu.add_command(label='Load data')
    Main_meniu.add_command(label='Save data')
    Main_meniu.add_command(label='Exit')

    #Pajamos, islaidos, balansas menu
    notebook = ttk.Notebook(Pagrindinis_langas)
    notebook.pack(fill="both", expand=True)

    tab_pajamos = Frame(notebook)
    tab_islaidos = Frame(notebook)
    tab_balansas = Frame(notebook)

    notebook.add(tab_pajamos, text="Pajamos")
    notebook.add(tab_islaidos, text="Išlaidos")
    notebook.add(tab_balansas, text="Balansas")

    #PAJAMOS FRAME----------------------------------------- 
    Pajamų_kat_label=Label(tab_pajamos, text='Pajamų kategorija:', font=('Arial', 12, 'bold'))
    Pajamų_kat_label.place(relx=0.02, rely=0.04)

    Pajamu_pasirinkimai=('Darbas', 'Savarankiška veikla', 'Custom', 't.t.')
    Pajamu_combo=ttk.Combobox(tab_pajamos, values=Pajamu_pasirinkimai, state='readonly')
    Pajamu_combo.current(0)
    Pajamu_combo.place(relx=0.025, rely=0.1)

    
    Iveskite_suma_lab=Label(tab_pajamos, text='Įveskite sumą:', font=('Arial', 12, 'bold'))
    Iveskite_suma_lab.place(relx=0.02, rely=0.2)

    Suma=Entry(tab_pajamos, justify='center')
    Suma.place(relx=0.025, rely=0.26)
    
    Data_lab=Label(tab_pajamos, text='Pasirinkite datą:', font=('Arial', 12, 'bold'))
    Data_lab.place(relx=0.02, rely=0.35)

    Data_ent=DateEntry(tab_pajamos, width=14, background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='y-mm-dd')
    Data_ent.place(relx=0.025, rely=0.40)

    #Buttons
    Prideti_myg=Button(tab_pajamos, text='Pridėti', command=lambda: add_pajamos(Suma.get(),Pajamu_combo.get(),Data_ent.get(),Tree))
    Prideti_myg.place(relx=0.02, rely=0.55, relwidth=0.25, relheight=0.1)

    Pasalinti_myg=Button(tab_pajamos, text='Pašalinti', command=lambda: remove_pajamos(Tree))
    Pasalinti_myg.place(relx=0.5, rely=0.55, relwidth=0.25, relheight=0.1)

    #Treeview
    Skyriai=('Data', 'Kategorija', 'Suma')

    Tree=ttk.Treeview(tab_pajamos, columns=Skyriai, show='headings')

    for i in Skyriai:
        Tree.heading(i, text=i)
        Tree.column(i, width=150, stretch=True)

    Tree.place(relx=0.25, rely=0.02, relwidth=0.6, relheight=0.4)

    pajamos=pajamu_sar()
    for paj in pajamos:
        Tree.insert('','end',values=(paj['laikas'],paj['paj_kategorija'],paj['money']))

    def remove_pajamos(Tree):
        pasirinkta=Tree.selection()
        if not pasirinkta:
            messagebox.showerror('Klaida','Pasirinkite kurį entry norite ištrinti.')
        for item in pasirinkta:
            values = Tree.item(item, "values")
            data, kat, money = values
            Tree.delete(item)
            delete_pajama(money,kat,data)

    Pagrindinis_langas.mainloop()

GUI()
