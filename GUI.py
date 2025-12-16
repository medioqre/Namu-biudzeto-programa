from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from data import *

def remove_pajamos(Tree):
    pasirinkta=Tree.selection()
    if not pasirinkta:
        messagebox.showerror('Klaida','Pasirinkite kurį entry norite ištrinti.')
    for item in pasirinkta:
        values = Tree.item(item, "values")
        data, kat, money = values
        Tree.delete(item)
        delete_pajama(money,kat,data) 
    #------------------refresh_charts()------------ cia idet

def rykiavimas_tree(tree,i,reverse):
    duomenys = [(tree.set(k, i), k) for k in tree.get_children("")]
    try:
        duomenys.sort(key=lambda t: float(t[0]), reverse=reverse)
    except ValueError:
        duomenys.sort(key=lambda t: t[0], reverse=reverse)
    for index, (val, k) in enumerate(duomenys):
        tree.move(k, "", index)
    tree.heading(i, command=lambda kop=i: rykiavimas_tree(tree, kop, not reverse))

def refresh_islaidu_tree(Tree):
    for i in Tree.get_children():
        Tree.delete(i)
    for isl in islaidu_sar():
        Tree.insert('','end',values=(isl["laikas"],isl['isl_kategorija'],isl['money'],isl['pavadinimas']))

def refresh_pajamu_tree(Tree):
    for i in Tree.get_children():
        Tree.delete(i)
    for paj in pajamu_sar():
        Tree.insert('','end',values=(paj["laikas"],paj['paj_kategorija'],paj['money']))

def refresh_balanso_label():
    pass
    #callint total balanse funkcija ir tada .config (text) ta label
   

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

    #PAJAMOS TAB----------------------------------------- 
    Pajamų_kat_label=Label(tab_pajamos, text='Pajamų kategorija:', font=('Arial', 12, 'bold'))
    Pajamų_kat_label.place(relx=0.02, rely=0.04)

    Pajamu_pasirinkimai=('Darbas', 'Savarankiška veikla', 'Custom', 't.t.')
    Pajamu_combo=ttk.Combobox(tab_pajamos, values=Pajamu_pasirinkimai, state='readonly')
    Pajamu_combo.current(0)
    Pajamu_combo.place(relx=0.025, rely=0.1)

    
    Iveskite_suma_lab=Label(tab_pajamos, text='Įveskite sumą:', font=('Arial', 12, 'bold'))
    Iveskite_suma_lab.place(relx=0.02, rely=0.2)

    paj_suma=Entry(tab_pajamos, justify='center')
    paj_suma.place(relx=0.025, rely=0.26)
    
    Data_lab=Label(tab_pajamos, text='Pasirinkite datą:', font=('Arial', 12, 'bold'))
    Data_lab.place(relx=0.02, rely=0.35)

    data_ent_paj=DateEntry(tab_pajamos, width=14, background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='y-mm-dd')
    data_ent_paj.place(relx=0.025, rely=0.40)

    def on_addpaj_click(Tree):
        if add_pajamos(paj_suma.get(),Pajamu_combo.get(),data_ent_paj.get()):
            pass
            refresh_pajamu_tree(Tree)
            #refresh_balance_label()
            #refresh_charts()

    #Buttons
    Prideti_myg=Button(tab_pajamos, text='Pridėti', font=('Arial', 12, 'bold'), command=lambda:on_addpaj_click(Tree))
    Prideti_myg.place(relx=0.02, rely=0.55, relwidth=0.25, relheight=0.1)

    Pasalinti_myg=Button(tab_pajamos, text='Pašalinti', font=('Arial', 12, 'bold'),  command=lambda: remove_pajamos(Tree)) 
    Pasalinti_myg.place(relx=0.3, rely=0.55, relwidth=0.25, relheight=0.1)

    #Treeview
    Skyriai=('Data', 'Kategorija', 'Suma')

    Tree=ttk.Treeview(tab_pajamos, columns=Skyriai, show='headings')

    for i in Skyriai:
        Tree.heading(i, text=i, command=lambda j=i: rykiavimas_tree(Tree, j, False))
        Tree.column(i, width=150, stretch=True)

    Tree.place(relx=0.25, rely=0.02, relwidth=0.6, relheight=0.4)

    pajamos=pajamu_sar()
    for paj in pajamos:
        Tree.insert('','end',values=(paj['laikas'],paj['paj_kategorija'],paj['money']))

    




    #IŠLAIDOS TAB-----------------------------------------

    Islaidu_kat_label=Label(tab_islaidos, text='Išlaidų kategorija:', font=('Arial', 12, 'bold'))
    Islaidu_kat_label.place(relx=0.02, rely=0.04)
    
    Islaidos_pasirinkimai=('Maistas', 'Transportas', 'Bendros', 't.t.')
    Islaidu_combo=ttk.Combobox(tab_islaidos, values=Islaidos_pasirinkimai, state='readonly')
    Islaidu_combo.current(0)
    Islaidu_combo.place(relx=0.025, rely=0.1)

    
    Iveskite_suma_lab=Label(tab_islaidos, text='Įveskite sumą:', font=('Arial', 12, 'bold'))
    Iveskite_suma_lab.place(relx=0.02, rely=0.2)

    isl_suma=Entry(tab_islaidos, justify='center')
    isl_suma.place(relx=0.025, rely=0.26)
    
    Data_islaidos_lab=Label(tab_islaidos, text='Pasirinkite datą:', font=('Arial', 12, 'bold'))
    Data_islaidos_lab.place(relx=0.02, rely=0.35)

    data_ent_isl=DateEntry(tab_islaidos, width=14, background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='y-mm-dd')
    data_ent_isl.place(relx=0.025, rely=0.40)

    def on_addisl_click(Tree):
        if add_islaidos(isl_suma.get(),Islaidu_combo.get(),data_ent_isl.get()):
            refresh_islaidu_tree(Tree)
            #refresh_balanso_label()
            #refresh_charts()

    #Buttons
    Prideti_islaidos_myg=Button(tab_islaidos, text='Pridėti', font=('Arial', 12, 'bold'),command = lambda: on_addisl_click(Tree))
    Prideti_islaidos_myg.place(relx=0.02, rely=0.55, relwidth=0.25, relheight=0.1)

    Pasalinti_islaidos_myg=Button(tab_islaidos, text='Pašalinti', font=('Arial', 12, 'bold'))
    Pasalinti_islaidos_myg.place(relx=0.3, rely=0.55, relwidth=0.25, relheight=0.1)

    #Treeview
    Skyriai_islaidos=('Data', 'Kategorija', 'Suma')

    Tree_islaidos=ttk.Treeview(tab_islaidos, columns=Skyriai_islaidos, show='headings')

    for col in Skyriai_islaidos:
        Tree_islaidos.heading(col, text=col)
        Tree_islaidos.column(col, width=150, stretch=True)

    Tree_islaidos.place(relx=0.25, rely=0.02, relwidth=0.6, relheight=0.4)
    


    #BALANSO TAB----------------------------------------------------
    balansas_lab=Label(tab_balansas, text=f'Balansas: {total_balansas()} Eur', font=('Arial', 12, 'bold'))
    balansas_lab.place(relx=0.43, rely=0.05)

    #Treeview balansas
    Skyriai_balansas=('Mėnesis', 'Pajamos', 'Išlaidos', 'Balansas')

    Tree_balansas=ttk.Treeview(tab_balansas, columns=Skyriai_balansas, show='headings')

    for col in Skyriai_balansas:
        Tree_balansas.heading(col, text=col)
        Tree_balansas.column(col, width=120, anchor='center', stretch=True)

    Tree_balansas.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.33)

    #Grafiku tabai
    graf_note=ttk.Notebook(tab_balansas)
    graf_note.place(relx=0.05, rely=0.40, relwidth=0.9, relheight=0.45)

    tab_menesiai = Frame(graf_note)
    tab_bar = Frame(graf_note)
    tab_pie = Frame(graf_note)

    graf_note.add(tab_menesiai, text='Mėnesiai')
    graf_note.add(tab_bar, text='"Bar" grafikas')
    graf_note.add(tab_pie, text='"Pie" grafikas')



    

    
    Pagrindinis_langas.mainloop()

GUI()
