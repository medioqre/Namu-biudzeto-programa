from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from data import *
from charts import bar,pie,menesiai
 
def GUI():
    def rykiavimas_tree(i,reverse):
        duomenys = [(Tree.set(k, i), k) for k in Tree.get_children("")]
        try:
            duomenys.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            duomenys.sort(key=lambda t: t[0], reverse=reverse)
        for index, (val, k) in enumerate(duomenys):
            Tree.move(k, "", index)
        Tree.heading(i, command=lambda kop=i: rykiavimas_tree(Tree, kop, not reverse))

    def refresh_islaidu_tree():
        for i in Tree.get_children():
            Tree.delete(i)
        for isl in list(islaidu_sar()):
            Tree.insert('','end',values=(isl["laikas"],isl['isl_kategorija'],isl['money'],isl['pavadinimas']))

    def refresh_pajamu_tree():
        for i in Tree.get_children():
            Tree.delete(i)
        for paj in pajamu_sar():
            Tree.insert('','end',values=(paj["laikas"],paj['paj_kategorija'],paj['money']))
        def refresh_balanso_label():
            newlabel=total_balansas()
            balansas_lab.config(text=f'Balansas: {total_balansas()} Eur')

    def remove_pajamos():
        pasirinkta=Tree.selection()
        if not pasirinkta:
            messagebox.showerror('Klaida','Pasirinkite kurį entry norite ištrinti.')
        for item in pasirinkta:
            values = Tree.item(item, "values")
            data, kat, money = values
            Tree.delete(item)
            delete_pajama(money,kat,data) 
        refresh_balanso_label()
        refresh_grafikus()

    def remove_islaidos():
        pasirinkta=Tree_islaidos.selection()
        if not pasirinkta:
            messagebox.showerror('Klaida','Pasirinkite kurį entry norite ištrinti.')
        for item in pasirinkta:
            values = Tree_islaidos.item(item, "values")
            pav,data, kat, money = values
            Tree_islaidos.delete(item)
            delete_islaida(pav,money,kat,data) 
        refresh_balanso_label()
        refresh_grafikus()

    #Pagrindinis langas
    Pagrindinis_langas=Tk()
    Pagrindinis_langas.title('Namų biudžeto skaičiuoklė')
    Pagrindinis_langas.geometry('900x700')

   

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
    Pajamų_kat_label.place(relx=0.025, rely=0.04)

    Pajamu_pasirinkimai=('Darbas', 'Savarankiška veikla', 'Custom', 't.t.')
    Pajamu_combo=ttk.Combobox(tab_pajamos, values=Pajamu_pasirinkimai, state='readonly')
    Pajamu_combo.current(0)
    Pajamu_combo.place(relx=0.03, rely=0.08)

    
    
    Iveskite_suma_lab=Label(tab_pajamos, text='Įveskite sumą:', font=('Arial', 12, 'bold'))
    Iveskite_suma_lab.place(relx=0.025, rely=0.13)

    paj_suma=Entry(tab_pajamos, justify='center')
    paj_suma.place(relx=0.03, rely=0.17)
    
    Data_lab=Label(tab_pajamos, text='Pasirinkite datą:', font=('Arial', 12, 'bold'))
    Data_lab.place(relx=0.025, rely=0.22)

    data_ent_paj=DateEntry(tab_pajamos, width=14, background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='y-mm-dd')
    data_ent_paj.place(relx=0.03, rely=0.26)

    def on_addpaj_click():
        if add_pajamos(paj_suma.get(),Pajamu_combo.get(),data_ent_paj.get()):
            refresh_pajamu_tree()
            refresh_balanso_label()
            refresh_grafikus()

    #Buttons
    Prideti_myg=Button(tab_pajamos, text='Pridėti', font=('Arial', 12, 'bold'), command=on_addpaj_click)
    Prideti_myg.place(relx=0.15, rely=0.55, relwidth=0.25, relheight=0.1)

    Pasalinti_myg=Button(tab_pajamos, text='Pašalinti', font=('Arial', 12, 'bold'),  command=remove_pajamos)
    Pasalinti_myg.place(relx=0.55, rely=0.55, relwidth=0.25, relheight=0.1)

    #Treeview
    Skyriai=('Data', 'Kategorija', 'Suma')
    Tree=ttk.Treeview(tab_pajamos, columns=Skyriai, show='headings')

    for i in Skyriai:
        Tree.heading(i, text=i, command=lambda j=i: rykiavimas_tree(Tree, j, False))
        Tree.column(i, width=80, stretch=True)

    Tree.place(relx=0.3, rely=0.02, relwidth=0.6, relheight=0.4)

    pajamos=pajamu_sar()
    for paj in pajamos:
        Tree.insert('','end',values=(paj['laikas'],paj['paj_kategorija'],paj['money']))

    




    #IŠLAIDOS TAB-----------------------------------------

    Islaidu_kat_label=Label(tab_islaidos, text='Išlaidų kategorija:', font=('Arial', 12, 'bold'))
    Islaidu_kat_label.place(relx=0.025, rely=0.04)
    
    Islaidos_pasirinkimai=('Maistas', 'Transportas', 'Bendros', 't.t.')
    Islaidu_combo=ttk.Combobox(tab_islaidos, values=Islaidos_pasirinkimai, state='readonly')
    Islaidu_combo.current(0)
    Islaidu_combo.place(relx=0.03, rely=0.08)

    Islaidu_pav_lab=Label(tab_islaidos, text='Pavadinimas', font=('Arial', 12, 'bold'))
    Islaidu_pav_lab.place(relx=0.025, rely=0.13)

    Islaidu_Pavadinimas=Entry(tab_islaidos, justify='center')
    Islaidu_Pavadinimas.place(relx=0.03, rely=0.17)

    
    Iveskite_suma_lab=Label(tab_islaidos, text='Įveskite sumą:', font=('Arial', 12, 'bold'))
    Iveskite_suma_lab.place(relx=0.025, rely=0.22)

    isl_suma=Entry(tab_islaidos, justify='center')
    isl_suma.place(relx=0.03, rely=0.26)
    
    Data_islaidos_lab=Label(tab_islaidos, text='Pasirinkite datą:', font=('Arial', 12, 'bold'))
    Data_islaidos_lab.place(relx=0.025, rely=0.31)

    data_ent_isl=DateEntry(tab_islaidos, width=14, background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='y-mm-dd')
    data_ent_isl.place(relx=0.03, rely=0.35)

    def on_addisl_click():
        if add_islaidos(isl_suma.get(),Islaidu_combo.get(),data_ent_isl.get(), Islaidu_Pavadinimas.get()):
            refresh_islaidu_tree()
            refresh_balanso_label()
            refresh_grafikus()

    #Buttons
    Prideti_islaidos_myg=Button(tab_islaidos, text='Pridėti', font=('Arial', 12, 'bold'),command = on_addisl_click)
    Prideti_islaidos_myg.place(relx=0.15, rely=0.55, relwidth=0.25, relheight=0.1)

    Pasalinti_islaidos_myg=Button(tab_islaidos, text='Pašalinti', font=('Arial', 12, 'bold'),command=remove_islaidos)
    Pasalinti_islaidos_myg.place(relx=0.55, rely=0.55, relwidth=0.25, relheight=0.1)

    #Treeview
    Skyriai_islaidos=('Pavadiniams', 'Data', 'Kategorija', 'Suma')

    Tree_islaidos=ttk.Treeview(tab_islaidos, columns=Skyriai_islaidos, show='headings')

    for col in Skyriai_islaidos:
        Tree_islaidos.heading(col, text=col)
        Tree_islaidos.column(col, width=130, stretch=True)

    Tree_islaidos.place(relx=0.3, rely=0.02, relwidth=0.6, relheight=0.4)
    
    islaidos=islaidu_sar()
    for isl in islaidos:
        Tree_islaidos.insert('','end',values=(isl['pavadinimas'],isl['laikas'],isl['isl_kategorija'],isl['money']))


    #BALANSO TAB----------------------------------------------------
    balansas_lab=Label(tab_balansas, text=f'Balansas: {total_balansas()} Eur', font=('Arial', 12, 'bold'))
    balansas_lab.place(relx=0.43, rely=0.05)

    def refresh_balanso_label():
        newlabel=total_balansas()
        balansas_lab.config(text=f'Balansas: {total_balansas()} Eur')

    #Treeview balansas
    Skyriai_balansas=('Mėnesis', 'Pajamos', 'Išlaidos', 'Balansas')

    Tree_balansas=ttk.Treeview(tab_balansas, columns=Skyriai_balansas, show='headings')

    for col in Skyriai_balansas:
        Tree_balansas.heading(col, text=col)
        Tree_balansas.column(col, width=120, anchor='center', stretch=True)

    Tree_balansas.place(relx=0.05, rely=0.10, relwidth=0.9, relheight=0.33)

    #Grafiku tabai
    graf_note=ttk.Notebook(tab_balansas)
    graf_note.place(relx=0.05, rely=0.40, relwidth=0.9, relheight=0.6)

    tab_menesiai = Frame(graf_note)
    tab_bar = Frame(graf_note)
    tab_pie = Frame(graf_note)

    # Funkcija nupiesia grafikus GUI lange pagal tabus + juos refreshina
    graf_note.add(tab_menesiai, text='Mėnesiai')
    graf_note.add(tab_bar, text='"Bar" grafikas')
    graf_note.add(tab_pie, text='"Pie" grafikas')

    # paspaudus ant kurio nors tabo grafikai refreshinas
    def refresh_grafikus():
        bar(tab_bar)
        pie(tab_pie)
        menesiai(tab_menesiai) 
    refresh_grafikus()

    Pagrindinis_langas.mainloop()

GUI()
