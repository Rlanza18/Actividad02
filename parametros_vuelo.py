# -*- coding: utf-8 -*-
"""
Created on Mon Feb  23 16:57:20 2022

@author: Raúl Lanza
"""


import tkinter as tk
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.geometry ("1030x700")
ventana.resizable(False,False)
ventana.config(bg="navajowhite2")

#Primera Fila

espacio = tk.Label(ventana, bg="navajowhite2", fg="navajowhite")
espacio.grid (row = 0, column = 0)

texto1 = tk.Label(ventana, text="Distancia Focal (mm)=", bg="navajowhite2", fg="gray20")
texto1.grid (row = 1, column = 0)

cuadro1 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro1.grid (row = 1, column = 1)

texto2 = tk.Label(ventana, text="Ancho del sensor (mm) =", bg="navajowhite2", fg="gray20")
texto2.grid (row = 1, column = 2)

cuadro2 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro2.grid (row = 1, column = 3)

texto3 = tk.Label(ventana, text="Solape Longitudinal (%)=", bg="navajowhite2", fg="gray20")
texto3.grid (row = 1, column = 4)

cuadro3 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro3.grid (row = 1, column = 5)

#SEGUNDA FILA

espacio1 = tk.Label(ventana, bg="navajowhite2", fg="navajowhite2")
espacio1.grid (row = 2, column = 0)

texto4 = tk.Label(ventana, text="Ancho de la imagen (Pixel)=", bg="navajowhite2", fg="gray20")
texto4.grid (row = 3, column = 0)

cuadro4 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro4.grid (row = 3, column = 1)

texto5 = tk.Label(ventana, text="Alto del sensor (mm)=", bg="navajowhite2", fg="gray20")
texto5.grid (row = 3, column = 2)

cuadro5 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro5.grid (row = 3, column = 3)

texto6 = tk.Label(ventana, text="Solape Transversal (%)=", bg="navajowhite2", fg="gray20")
texto6.grid (row = 3, column = 4)

cuadro6 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro6.grid (row = 3, column = 5)

#Tercera Fila

espacio2 = tk.Label(ventana, bg="navajowhite2", fg="gray20")
espacio2.grid (row = 4, column = 0)

texto7 = tk.Label(ventana, text="Alto de la imagen (Pixel) =", bg="navajowhite2", fg="gray20")
texto7.grid (row = 5, column = 0)

cuadro7 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro7.grid (row = 5, column = 1)

texto8 = tk.Label(ventana, text="Altura del vuelo (m)=", bg="navajowhite2", fg="gray20")
texto8.grid (row = 5, column = 2)

cuadro8 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro8.grid (row = 5, column = 3)

texto9 = tk.Label(ventana, text="Largo de la parcela (m)=", bg="navajowhite2", fg="gray20")
texto9.grid (row = 5, column = 4)

cuadro9 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro9.grid (row = 5, column = 5)

#Cuarta Fila

espacio3 = tk.Label(ventana, bg="navajowhite2", fg="gray20")
espacio3.grid (row = 6, column = 0)

texto10 = tk.Label(ventana, text="Ancho de la parcela (m)=", bg="navajowhite2", fg="gray20")
texto10.grid (row = 7, column = 0)

cuadro10 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro10.grid (row = 7, column = 1)

texto11 = tk.Label(ventana, text="Velocidad del vuelo (m/s)=", bg="navajowhite2", fg="gray20")
texto11.grid (row = 7, column = 2)

cuadro11 = tk.Entry(ventana, font = "Cambria 12", justify = "left")
cuadro11.grid (row = 7, column = 3)

espacio3 = tk.Label(ventana, bg="navajowhite2", fg="navajowhite2")
espacio3.grid (row = 8, column = 0)


espacio3 = tk.Label(ventana, bg="navajowhite2", fg="coral")
espacio3.grid (row = 10, column = 0)

#Resultados
textoResult = tk.Text(ventana)
textoResult.grid(row = 11, column = 0, columnspan = 6)

#Cálculo 

def resultados():
    textoResult.delete(1.0, tk.END)
    d_focal = float(cuadro1.get())
    ancho_sensor = float(cuadro2.get())
    solape_long = float(cuadro3.get())
    ancho_img = float(cuadro4.get())
    altura_sensor = float(cuadro5.get())
    RSI = ancho_sensor/ancho_img
    solape_trans = float(cuadro6.get())
    altura_img = int(cuadro7.get())
    altura_vuelo = float(cuadro8.get())
    largo_parcela = float(cuadro9.get())
    ancho_parcela = float(cuadro10.get())
    vel_vuelo = float(cuadro11.get())
    
    
    #GSD
    GSD = (((altura_vuelo * 100 )/ (d_focal)) * RSI)
    textoResult.insert(tk.END, f"GSD = {GSD}cm/pixel\n\n")
    
    #Escala de Vuelo
    escala_vuelo = 1/((d_focal/1000)/altura_vuelo)
    textoResult.insert(tk.END, f"Escala de vuelo = {escala_vuelo}\n\n")
    
    #Ancho de la imagen
    areatomada = (ancho_sensor*escala_vuelo)/1000
    textoResult.insert(tk.END, f"Ancho de la Imagen Sobre el Terreno = {areatomada}m\n\n")
    
    #Alto de la imagen
    areatomada = (altura_sensor*escala_vuelo)/1000
    textoResult.insert(tk.END, f"Alto de la Imagen Sobre el Terreno = {areatomada}m\n\n")
    
    #Base Aérea
    base_aer = (((ancho_img * GSD )/100)* (1-(solape_long/100)))
    textoResult.insert(tk.END, f"Base Aérea = {base_aer}\n\n")
    
    #Distancia entre vueltas
    Dist_vueltas = (((altura_img * GSD )/100)) * (1-(solape_trans/100))
    textoResult.insert(tk.END, f"Distancia entre vueltas = {Dist_vueltas}m\n\n")
    
    #Tiempo entre fotos y velocidad de vuelo
    tiem_fotos = base_aer/vel_vuelo
    vel_vuelo= base_aer/tiem_fotos
    textoResult.insert(tk.END, f"Tiempo entre fotos = {tiem_fotos}s\n\n")
    textoResult.insert(tk.END, f"Velocidad de Vuelo= {vel_vuelo}m/s\n\n")
    
    #Número de pasadas
    num_pasadas = round (ancho_parcela/Dist_vueltas)
    textoResult.insert(tk.END, f"Numero de pasadas = {num_pasadas}\n\n")
    
    #Número de fotos por vueltas
    num_fotos = round (largo_parcela/base_aer)+1
    textoResult.insert(tk.END, f"Numero de Fotos por vueltas = {num_fotos}\n\n")
    
    #Número de fotos por pasada
    num_vuelta= round (num_fotos)*(num_pasadas)+1
    textoResult.insert(tk.END, f"Numero de Fotos por Vuelo = {num_vuelta}\n\n")
    
    #Distancia de Vuelo
    dist_vuelo = (num_pasadas*largo_parcela)+ancho_parcela
    textoResult.insert(tk.END, f"Distancia de Vuelo = {dist_vuelo}m\n\n")
    
    #Duración de vuelo 
    t_vuelo= ((num_vuelta * tiem_fotos)/60)
    textoResult.insert(tk.END, f"Duracion del Vuelo = {t_vuelo}min")
    
    popup_showinfo()

#Ventana Emergente
def popup_showinfo():
    message ="¡finalizado!"
    showinfo(message)
    
#Botón de Cálculo (con cambio de color incluido)
boton_calculo = tk.Button(text = "Calcular", font= 'Cambria 11', command = resultados)
boton_calculo.grid(row = 9, column = 2, columnspan = 2)


#Título 
ventana.title("Calculadora de parámetros de vuelo de drone")

ventana.mainloop()