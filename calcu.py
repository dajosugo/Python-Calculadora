# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:24:49 2021

@author: dajos
"""
from tkinter import *
from math import *
 
#VISUALIZAR LA OPERACION EN LA PANTALLA
def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)
    input_text2.set(input_text2.get()+operador+"\n")
    label = Label(ventana,relief="solid", width=18,height=10,  fg="black", bg="gray77",textvariable=input_text2).place(x=470,y=30)
    
    
 
#CÁLCULO Y MUESTRA DE RESULTADOS.
def resultado():
    global operador
    try:
        opera=str(eval(operador))
        operador=opera
        input_text.set(operador)
        input_text2.set(input_text2.get()+operador+"\n")
        label = Label(ventana,width=18,height=10,  fg="black", bg="gray77",textvariable=input_text2).place(x=470,y=30)
    except:
        input_text.set("ERROR")
        operador = ""
 
#LIMPIEZA DE PANTALLA.
def clear():
    global operador
    operador=("")
    input_text.set("0")   

    
#Cambiar signo
def cambia_signo(): 
    global operador
    global l_operadores
    if operador!="0" and operador!="":
        operador=str(eval(operador+"*(-1)"))
        input_text.set(operador)
    elif operador=="" and len(l_operadores)==1: #nuevo
        if l_operadores[0]!="0":
            l_operadores[0]=str(eval(l_operadores[0]+"*(-1)"))
            input_text.set(l_operadores[0]) 
            

#borrar un error
def clear_error():
    global operador
    if operador!="0" and operador!="":
        operador = operador[:-1]
        input_text.set(operador)

ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("600x600")
ventana.configure(background="SkyBlue4")
color_boton=("gray77")
 
ancho_boton=11
alto_boton=3
input_text=StringVar()
input_text2=StringVar()
operador=""
l_operadores=[]


Salida=Entry(ventana,font=('arial',20,'bold'),width=27,
textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right")
Salida.place(x=10,y=60)


#historial

 
#AÑADIR BOTONES.
#CREAMOS NUESTROS BOTONES
Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=197,y=500)
Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=107,y=440)
Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=197,y=440)
Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=287,y=440)
Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=107,y=380)
Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=197,y=380)
Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=287,y=380)
Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=107,y=320)
Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=197,y=320)
Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=287,y=320)
Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(".")).place(x=287,y=500)
Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=377,y=440)
Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=377,y=380)
Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=377,y=320)
Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=377,y=260)
Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado).place(x=377,y=500)
Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=107,y=260)
Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=197,y=260)
Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear).place(x=287,y=140)
Button(ventana,text="⟵",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear_error).place(x=377,y=140)
Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("3,14159")).place(x=107,y=140)
Button(ventana,text="e",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("2,71828")).place(x=197,y=140)
Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("E")).place(x=287,y=200)
Button(ventana,text="+/-",bg=color_boton,width=ancho_boton,height=alto_boton,command=cambia_signo).place(x=107,y=500)
Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log(")).place(x=17,y=440)
Button(ventana,text="log",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("log10(")).place(x=17,y=500)
Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("sqrt(")).place(x=17,y=260)
Button(ventana,text="1/x",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("1/")).place(x=107,y=200)
Button(ventana,text="n!",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("factorial(")).place(x=287,y=260)
Button(ventana,text="|x|",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("abs(")).place(x=197,y=200)
Button(ventana,text="^2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**2")).place(x=17,y=200)
Button(ventana,text="x^y",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("**")).place(x=17,y=320)
Button(ventana,text="10^x",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("10**")).place(x=17,y=380)
Button(ventana,text="mod",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("%")).place(x=377,y=200)

clear()
 
ventana.mainloop()