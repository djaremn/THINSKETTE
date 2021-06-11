# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 17:11:23 2021

@author: Djaremn
"""

import PySimpleGUI as simpleg

# Creamos el diseño de la ventana
layout = [[simpleg.Text('Hola Thinskette')], [simpleg.Button('No me apretes :$')]]


# Creamos la ventana
window = simpleg.Window(title='Thinskette', layout=layout,
          margins=(400,280))

#Creamos un loop para definir los evnetos que cierren la ventana

while True:
    event, values = window.read()
    # Finaliza la ventana si se cierra o si se aprete lo que deberia ser el OK
    if event == 'No me apretes :$' or event == simpleg.WIN_CLOSED:
        break
    
window.close()
        
