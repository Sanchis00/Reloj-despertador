'''Script que simula un Reloj despertador que, en lugar de reproducir una melodía
como alarma, reproduce un video de Youtube aleatorio contenido en una lista
de URL's'''

# Importamos los módulos necesarios

from tkinter import * # Tkinter para la interfaz gráfica
from tkinter import messagebox, ttk # Para usar combobox
from urllib import request # Urlllib para trabajar con las URL's
from time import strftime # Time para manejar el tiempo
import random
import webbrowser




# Programa principal
# ventana principal

screen = Tk()
screen.title("Reloj Despertador")
screen.geometry("500x500")
screen.config(bg = 'black')
screen.minsize(width=500,height=500)
screen.maxsize(width=500,height=500)

# Listas que almacenan las variables

lista_horas = []

lista_minutos = []

lista_segundos = []


for i in range(0,24):
    lista_horas.append(i)

for i in range(0,60):
    lista_minutos.append(i)

for i in range(0,60):
    lista_segundos.append(i)


# Etiquetas
# horas

horas = Label(screen,text='Horas',fg="pink",bg='gray',font=("Helvetica",12,'bold'))
horas.grid(row=1,column=0,padx=5,pady=5)


minutos = Label(screen,text='Minutos',fg="pink",bg='gray',font=("Helvetica",12,'bold'))
minutos.grid(row=1,column=1,padx=5,pady=5)


segundos = Label(screen,text='Segundos',fg="pink",bg='gray',font=("Helvetica",12,'bold'))
segundos.grid(row=1,column=2,padx=5,pady=5)


# Cajas para elegir la hora de colocación de alarma

caja_horas = ttk.Combobox(screen,values=lista_horas,style = "TCombobox",justify = 'center',width=11,font='Arial')
caja_horas.grid(row=2,column=0,padx=12,pady=5)
caja_horas.current(0)

caja_minutos = ttk.Combobox(screen,values=lista_minutos,style = "TCombobox",justify = 'center',width=11,font='Arial')
caja_minutos.grid(row=2,column=1,padx=12,pady=5)
caja_minutos.current(0)


caja_segundos = ttk.Combobox(screen,values=lista_segundos,style = "TCombobox",justify = 'center',width=11,font='Arial')
caja_segundos.grid(row=2,column=2,padx=12,pady=5)
caja_segundos.current(0)


# Estilo combobox

style = ttk.Style()
style.theme_create('combostyle', parent='alt',settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'red',
                                       'fieldbackground': 'gold',
                                       'background': 'blue'
                                       }}})
style.theme_use('combostyle')

screen.option_add('*TCombobox*Listbox*Background', 'white')
screen.option_add('*TCombobox*Listbox*Foreground', 'black')
screen.option_add('*TCombobox*Listbox*selectBackground', 'green2')
screen.option_add('*TCombobox*Listbox*selectForeground', 'black')




# Etiquetas para la interfaz de la alarma

e_alarma = Label(screen,text=0,bg = 'black',fg = 'pink',font=('Radioland',25))
e_alarma.grid(row=4,columnspan=3,ipady=30,ipadx=5)


# Archivo url
filename = 'url.txt'

with open(filename,'r') as f:
    lineas = f.readlines()
    eleccion = random.choice(lineas)

# FUNCIONES PRINCIPALES
    

def reloj():

    hora_input = caja_horas.get()
    minutos_input = caja_minutos.get()
    segundos_input = caja_segundos.get()

    hora_x = strftime('%H')
    min_x = strftime('%M')
    sec_x= strftime('%S')

    hora_main = (hora_x + ' : ' + min_x + ' : ' + sec_x)
    e_reloj.config(text=hora_main,font=('Radioland',20))

    hora_alarma = hora_input + ' : ' + minutos_input + ' : ' + segundos_input
    e_alarma['text'] = hora_alarma

    if int(hora_input) == int(hora_x):
        if int(minutos_input) == int(min_x):
            if int(segundos_input) == int(sec_x):
                messagebox.showinfo(title="Alarma",message=f"Alarma activada")
                webbrowser.open(eleccion)


    e_reloj.after(100,reloj)

    


# Etiqueta que representa el RELOJ

e_reloj = Label(screen,fg='pink',bg='black')
e_reloj.grid(row=0,columnspan=3,ipady=10,ipadx=5)

reloj()
screen.mainloop()