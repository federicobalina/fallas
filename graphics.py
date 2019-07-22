from tkinter import *
 
from tkinter.ttk import *

class RadioButtons:
    def __init__(self, window, label, column, row, values):
        self.buttons = []
        self.selected = IntVar()
        
        lbl = Label(window, text=label)
        lbl.grid(column=column, row=row)
        current_column = column + 1
        for text,value in values:
            button = Radiobutton(window, text=text, value=value, variable=self.selected )
            button.grid(column = current_column, row=row)
            current_column += 1

class RadioButtons_1_to_5(RadioButtons):
    def __init__(self, window, label, column, row):
        values = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
        super().__init__(window, label, column, row, values)

class RadioButtons_yes_or_no(RadioButtons):
    def __init__(self, window, label, column, row):
        values = [('Sí', True), ('No', False)]
        super().__init__(window, label, column, row, values)

window = Tk()
 
window.title("Detección de Tuberculosis")

buttons = {} 
buttons['sistema_respiratorio'] = RadioButtons_1_to_5(window, 'Tos, mocos, dificultad al respirar', 0, 0)
buttons['contacto_social'] = RadioButtons_1_to_5(window, 'Contacto social', 0, 1)
buttons['exposicion'] = RadioButtons_1_to_5(window, 'Exposición a Tuberculosis', 0, 2)
buttons['sudores_nocturnos'] = RadioButtons_yes_or_no(window, "Sudores nocturnos", 0, 3)
buttons['astenia'] = RadioButtons_1_to_5(window, 'Sensación de debilidad, fatiga general', 0, 4)
buttons['adinamia'] = RadioButtons_1_to_5(window, 'Ausencia de fuerza física', 0, 5)
buttons['hiporexia'] = RadioButtons_1_to_5(window, 'Disminución del apetito', 0, 6)
buttons['alimentacion'] = RadioButtons_1_to_5(window, 'Mala alimentación', 0, 7)
buttons['salubridad'] = RadioButtons_1_to_5(window, 'Condiciones insalubres', 0, 8)
buttons['hiv'] = RadioButtons_yes_or_no(window, 'Portador HIV', 0, 9)
buttons['inmunodeficiencia'] = RadioButtons_yes_or_no(window, 'Inmunodeficiencia', 0, 10)
buttons['inmunosupresion'] = RadioButtons_1_to_5(window, "Consumo de medicamentos inmunosupresores", 0 , 11)
buttons['bcg'] = RadioButtons_yes_or_no(window, "Vacuna BCG", 0, 12)
buttons['bacilos_esputo'] = RadioButtons_yes_or_no(window, "Bacilos en esputo", 0, 13)
buttons['bacilos_secrecion'] = RadioButtons_yes_or_no(window, "Bacilos en cultivo de secreción", 0, 14)

window.mainloop()