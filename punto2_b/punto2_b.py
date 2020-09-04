import tkinter as tk
from tkinter import ttk,messagebox
global data_tabla

cols=["N","Peso","Precio"]
cols_2=["N Equipajes","Peso max","Peso min","Peso prom","Ingreso (peso)","Ingresos (dolar)"]
approx_capacaity = 18000
m_bulto=500
dolar=3700
data_tabla=[]


def peso_limite(bulto):
    if len(data_tabla)==0:
        precio_bulto(bulto)
    elif len(data_tabla)>0:
        if sum( [ k[0] for k in data_tabla ] )< approx_capacaity:
            precio_bulto(bulto)
        else:
            messagebox.showerror("Error", "El peso del equipaje excede la capacidad del avión")



def precio_bulto(bulto):
    try:
        bulto=int(bulto)
        if (bulto>=0) and (bulto<=500):
            precio=0
            if (bulto>=0) and  (bulto<=25):
                precio=0
            elif (bulto>=26) and (bulto<=300):
                precio= 1500*bulto
            else:
                precio= 2500*bulto
            data_tabla.append([bulto,precio])
        
            
        else:
            text_bulto.delete(0, 'end')
            messagebox.showerror("Error", "El valor ingresado excede el límite de peso por equipaje")
        show()
        resumen()

    except ValueError:
        
        messagebox.showerror("Error", "Valor ingresado no es valido, debe ser numero entero.")
        text_bulto.delete(0, 'end')

def show():
    for i in listBox.get_children():
        listBox.delete(i)
    for i, (peso, precio) in enumerate(data_tabla, start=1):
        listBox.insert("", "end", values=(i, peso, precio))

def resumen():
    list_resumen.insert("", 0,values=(len(data_tabla),
                                            max( [ k[0] for k in data_tabla ] ),
                                            min( [k[0] for k in data_tabla ] ),
                                            sum( [ k[0] for k in data_tabla ] ) / len(data_tabla),
                                            sum( [ k[1] for k in data_tabla ] ),
                                            sum( [k[1] for k in data_tabla] ) * dolar
                                            ))

def delete():
    for i in listBox.get_children():
        listBox.delete(i)
    for j in list_resumen.get_children():
        list_resumen.delete(j)
    text_bulto.delete(0, 'end')


######APLICACION#####
master = tk.Tk() ###raiz
master.title("Gestion de equipaje ")

frame_bulto=tk.LabelFrame(master,text="Peso (Kg)")
frame_bulto.grid(column=5,row=1,padx=20,pady=5)

text_bulto=tk.Entry( frame_bulto,font=("Consolas", 8))
text_bulto.grid(column=5,row=1,padx=5,pady=5)


frame_buttons=tk.LabelFrame(master,text="Botones")
frame_buttons.grid(column=5,row=5,padx=20,pady=5)

button_bulto=tk.Button(frame_buttons,text="Cargar", 
                        height=2,width =15, 
                        command=(lambda: peso_limite(text_bulto.get())))
button_bulto.grid(column=1,row=1, padx=10,pady=5)


button_borrar=tk.Button(frame_buttons,text="Borrar", height =2,width = 15,command=delete)
button_borrar.grid(column=3,row=1, padx=10,pady=5)


listBox= ttk.Treeview(master, columns=cols, show='headings')
listBox.column(cols[0], minwidth=0, width=100, stretch=False)
listBox.column(cols[1], minwidth=0, width=200, stretch=False)
listBox.column(cols[2], minwidth=0, width=200, stretch=False)

for col in cols:
    listBox.heading(col, text=col)
listBox.grid(column=5,row= 3,columnspan=2)


scroll_log=tk.Scrollbar(master,command=listBox.yview,width=15)
listBox.config(yscrollcommand=scroll_log.set)
scroll_log.grid(row=3,column=7,sticky="nsew")

list_resumen= ttk.Treeview(master, columns=cols_2, show='headings',height = 1)
for col in cols_2:
    list_resumen.column(col, minwidth=0, width=100, stretch=False) 
    list_resumen.heading(col, text=col)
list_resumen.grid(column=5,row= 4,columnspan=2)
    

tk.mainloop()