from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from data import *
from charts import bar,pie,menesiai
 
def GUI():
    def rykiavimas_tree(Tree,i,reverse):
        duomenys = [(Tree.set(k, i), k) for k in Tree.get_children("")]
        try:
            duomenys.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            duomenys.sort(key=lambda t: t[0], reverse=reverse)
        for index, (val, k) in enumerate(duomenys):
            Tree.move(k, "", index)
        Tree.heading(i, command=lambda kop=i: rykiavimas_tree(kop, not reverse))

    def refresh_islaidu_tree():
        for i in Tree_islaidos.get_children():
            Tree_islaidos.delete(i)
        for isl in islaidu_sar():
            Tree_islaidos.insert('','end',values=(isl["pavadinimas"],isl['laikas'],isl['isl_kategorija'],isl['money']))

    def refresh_pajamu_tree():
        for i in Tree.get_children():
            Tree.delete(i)
        for paj in pajamu_sar():
            Tree.insert('','end',values=(paj["laikas"],paj['paj_kategorija'],paj['money']))

    def refresh_balanso_tree():
        for i in Tree_balansas.get_children():
            Tree_balansas.delete(i)
        pajamos = menesio_pajamos()
        islaidos = menesio_islaidos()
        balansas = menesio_balansas()
        men = gaut_menesius()
        for m in men:
            paj = pajamos.get(m, 0)
            isl = islaidos.get(m, 0)
            bal = balansas.get(m, 0)
            Tree_balansas.insert('','end',values=(m,paj,isl,bal))

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
        refresh_balanso_tree()

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
        refresh_balanso_tree()

    #Pagrindinis langas
    Pagrindinis_langas=Tk()
    Pagrindinis_langas.title('Namų biudžeto skaičiuoklė')
    Pagrindinis_langas.minsize(620, 750)


   

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

    left = ttk.Frame(tab_pajamos)
    right = ttk.Frame(tab_pajamos)
    
    left.grid(row=0, column=0, sticky="n", padx=10, pady=10)
    right.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    tab_pajamos.columnconfigure(1, weight=1)
    tab_pajamos.rowconfigure(0, weight=1)

    right.columnconfigure(0, weight=1)
    right.rowconfigure(0, weight=1)



    Pajamų_kat_label=Label(left, text='Pajamų kategorija:', font=('Arial', 12, 'bold'))
    Pajamų_kat_label.grid(row=0, column=0, sticky="w",pady=5,padx=5)

    Pajamu_pasirinkimai=('Darbas', 'Savarankiška veikla', 'Custom', 't.t.')
    Pajamu_combo=ttk.Combobox(left, values=Pajamu_pasirinkimai, state='readonly')
    Pajamu_combo.current(0)
    Pajamu_combo.grid(row=1, column=0, sticky="we",pady=5,padx=5)

    
    
    Iveskite_suma_lab=Label(left, text='Įveskite sumą:', font=('Arial', 12, 'bold'))
    Iveskite_suma_lab.grid(row=2, column=0, sticky="w",pady=5,padx=5)

    paj_suma=Entry(left, justify='center')
    paj_suma.grid(row=3, column=0, sticky="we",pady=5,padx=5)
    
    Data_lab=Label(left, text='Pasirinkite datą:', font=('Arial', 12, 'bold'))
    Data_lab.grid(row=4, column=0, sticky="w",pady=5,padx=5)

    data_ent_paj=DateEntry(left, width=14, background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='y-mm-dd')
    data_ent_paj.grid(row=5, column=0, sticky="w",pady=5,padx=5)

    def on_addpaj_click():
        if add_pajamos(paj_suma.get(),Pajamu_combo.get(),data_ent_paj.get()):
            refresh_pajamu_tree()
            refresh_balanso_label()
            refresh_grafikus()
            paj_suma.delete(0,END) 
            refresh_balanso_tree()
    #Buttons
    Prideti_myg=Button(left, text='Pridėti', font=('Arial', 12, 'bold'), command=on_addpaj_click)
    Prideti_myg.grid(row=6, column=0, sticky="we",pady=5,padx=5)

    Pasalinti_myg=Button(right, text='Pašalinti', font=('Arial', 12, 'bold'),  command=remove_pajamos) 
    Pasalinti_myg.grid(row=1, column=0,pady=5,padx=5)

    #Treeview
    Skyriai=('Data', 'Kategorija', 'Suma')

    Tree=ttk.Treeview(right, columns=Skyriai, show='headings')

    for i in Skyriai:
        Tree.heading(i, text=i, command=lambda j=i: rykiavimas_tree(j, False))
        Tree.column(i, width=80, stretch=True)

    Tree.grid(row=0, column=0, sticky="nsew",pady=5,padx=5)

    pajamos=pajamu_sar()
    for paj in pajamos:
        Tree.insert('','end',values=(paj['laikas'],paj['paj_kategorija'],paj['money']))
    




    #IŠLAIDOS TAB-----------------------------------------
    leftisl = ttk.Frame(tab_islaidos)
    rightisl = ttk.Frame(tab_islaidos)
    
    leftisl.grid(row=0, column=0, sticky="n", padx=10, pady=10)
    rightisl.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    tab_islaidos.columnconfigure(1, weight=1)
    tab_islaidos.rowconfigure(0, weight=1)

    rightisl.columnconfigure(0, weight=1)
    rightisl.rowconfigure(0, weight=1)

    Islaidu_kat_label=Label(leftisl, text='Išlaidų kategorija:', font=('Arial', 12, 'bold'))
    Islaidu_kat_label.grid(row=0, column=0, sticky="w",pady=5,padx=5)
    
    Islaidos_pasirinkimai=('Maistas', 'Transportas', 'Bendros', 't.t.')
    Islaidu_combo=ttk.Combobox(leftisl, values=Islaidos_pasirinkimai, state='readonly')
    Islaidu_combo.current(0)
    Islaidu_combo.grid(row=1, column=0, sticky="we",pady=5,padx=5)

    Islaidu_pav_lab=Label(leftisl, text='Pavadinimas', font=('Arial', 12, 'bold'))
    Islaidu_pav_lab.grid(row=2, column=0, sticky="w",pady=5,padx=5)

    Islaidu_Pavadinimas=Entry(leftisl, justify='center')
    Islaidu_Pavadinimas.grid(row=3, column=0, sticky="we",pady=5,padx=5)
    
    Iveskite_suma_lab=Label(leftisl, text='Įveskite sumą:', font=('Arial', 12, 'bold'))
    Iveskite_suma_lab.grid(row=4, column=0, sticky="w",pady=5,padx=5)

    isl_suma=Entry(leftisl, justify='center')
    isl_suma.grid(row=5, column=0, sticky="we",pady=5,padx=5)
    
    Data_islaidos_lab=Label(leftisl, text='Pasirinkite datą:', font=('Arial', 12, 'bold'))
    Data_islaidos_lab.grid(row=6, column=0, sticky="w",pady=5,padx=5)

    data_ent_isl=DateEntry(leftisl, width=14, background='darkblue', foreground='white', borderwidth=2, year=2025, date_pattern='y-mm-dd')
    data_ent_isl.grid(row=7, column=0, sticky="w",pady=5,padx=5)

    def on_addisl_click():
        if add_islaidos(isl_suma.get(),Islaidu_combo.get(),data_ent_isl.get(), Islaidu_Pavadinimas.get()):
            refresh_islaidu_tree()
            refresh_balanso_label()
            refresh_grafikus()
            refresh_balanso_tree()
            isl_suma.delete(0,END) 
            Islaidu_Pavadinimas.delete(0,END)

    #Buttons
    Prideti_islaidos_myg=Button(leftisl, text='Pridėti', font=('Arial', 12, 'bold'),command = on_addisl_click)
    Prideti_islaidos_myg.grid(row=8, sticky='ew',pady=5,padx=5)

    Pasalinti_islaidos_myg=Button(tab_islaidos, text='Pašalinti', font=('Arial', 12, 'bold'), command=remove_islaidos)
    Pasalinti_islaidos_myg.grid(row=1,column=1)

    #Treeview
    Skyriai_islaidos=('Pavadiniams', 'Data', 'Kategorija', 'Suma')

    Tree_islaidos=ttk.Treeview(rightisl, columns=Skyriai_islaidos, show='headings')

    for col in Skyriai_islaidos:
        Tree_islaidos.heading(col, text=col)
        Tree_islaidos.column(col, width=80, stretch=True)

    Tree_islaidos.grid(row=0, sticky='nsew') 
    
    islaidos=islaidu_sar()
    for isl in islaidos:
        Tree_islaidos.insert('','end',values=(isl['pavadinimas'],isl['laikas'],isl['isl_kategorija'],isl['money']))


    #BALANSO TAB----------------------------------------------------
    balansas_lab=Label(tab_balansas, text=f'Balansas: {total_balansas()} Eur', font=('Arial', 16, 'bold'))
    balansas_lab.grid(row=0,column=0,pady=5,padx=3)

    tab_balansas.columnconfigure(0, weight=1)
    tab_balansas.rowconfigure(1, weight=1)  # Treeview row
    tab_balansas.rowconfigure(3, weight=3)  # Graphs row (bigger)


    def refresh_balanso_label():
        newlabel=total_balansas()
        balansas_lab.config(text=f'Balansas: {total_balansas()} Eur')

    #Treeview balansas
    Skyriai_balansas=('Mėnesis', 'Pajamos', 'Išlaidos', 'Balansas')

    Tree_balansas=ttk.Treeview(tab_balansas, columns=Skyriai_balansas, show='headings')
    refresh_balanso_tree()

    for i in Skyriai_balansas:
        Tree_balansas.heading(i, text=i, command=lambda j=i: rykiavimas_tree(Tree_balansas, j, False))
        Tree_balansas.column(i, width=120, anchor='center', stretch=True)

    Tree_balansas.grid(row=1,column=0,pady=5,padx=3,sticky='nsew')

    #Grafiku tabai
    graf_note=ttk.Notebook(tab_balansas)
    graf_note.grid(row=2,column=0,pady=5,padx=3,sticky='nsew')

    tab_menesiai = Frame(graf_note)
    tab_bar = Frame(graf_note)
    tab_pie = Frame(graf_note)

    # Funkcija nupiesia grafikus GUI lange pagal tabus + juos refreshina
    graf_note.add(tab_menesiai, text='Mėnesio balansai')
    graf_note.add(tab_bar, text='Mėnesių pajamos ir išlaidos')
    graf_note.add(tab_pie, text='Išlaidos pagal kategorijas')

    def refresh_grafikus():
        bar(tab_bar)
        pie(tab_pie)
        menesiai(tab_menesiai) 
    refresh_grafikus()

    Pagrindinis_langas.mainloop()

GUI()
