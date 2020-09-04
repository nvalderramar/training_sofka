import tkinter as tk #Libreria interfaz grafica
from tkinter import messagebox #función de errores tk 

def price_calculate(distance,time_instance,px_km=35):
    try:
        d=int(distance)
        t=int(time_instance)
        if (d<0) or (t<0):
            messagebox.showerror("Error", "los valores ingresados deben ser positivos.")
            text_dist.delete(0, 'end')
            text_time_instance.delete(0, 'end')
        else:
            price_temporal= (d*px_km)
            if (d > 1000) and (t > 7):
                price=price_temporal*0.7
            else:
                price=price_temporal
    
            text_output.configure(text=str(price))
    except ValueError:
        
        messagebox.showerror("Error", "valor ingresado no es valido, debe ser número entero.")
        text_dist.delete(0, 'end')
        text_time_instance.delete(0, 'end')
######APLICACION#####
master = tk.Tk() ###raiz
master.title("Caculadora de valor de pasaje en avión ")

label_dist= tk.Label(master, text="Distancia")
label_dist.grid(column=1,row=1,padx=10,pady=5)
label_dist.config(fg="blue")

label_time_instance= tk.Label(master, text="Tiempo de instancia")
label_time_instance.grid(column=1,row=3,padx=10,pady=5)
label_time_instance.config(fg="blue")

text_dist=tk.Entry ( master,font=("Consolas", 8))
text_dist.grid(column=3,row=1,padx=10,pady=5)

text_time_instance=tk.Entry ( master ,font=("Consolas", 8))
text_time_instance.grid(column=3,row=3,padx=10,pady=5)

button_price=tk.Button(master,text="Calcular valor del vuelo",
                            command=(lambda: price_calculate(text_dist.get(),text_time_instance.get())))
button_price.grid(column=1,row=5, padx=10,pady=5)


text_output= tk.Label( master ,width=20,height=2,font=("Consolas", 8))
text_output.grid(column=3,row=5, padx=10,pady=5)

tk.mainloop()
