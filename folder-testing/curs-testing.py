'''# --------------------- Interfata Grafica (GUI) --------------------- '''

import tkinter

# Definire obiect pentru interfata si detaliile acesteia ----------------------------

window = tkinter.Tk()
window.title("First interface !")
window.geometry ("400x300") # wide x width pentru fereastra
window.resizable (False,False) # dam sau nu posibilitatea de a schimba dimensiunea ferestrei


# Adaugare widgets (text, user input, button) ----------------------------

# tkinter.Label(window, text="Hello, my name is Jeff").pack() # adaugam un text pe mijoloc by default

# user_input = tkinter.Entry(window) # adauga un camp pentru completare text
# user_input.pack()

# def greet(): 
#     tkinter.Label(window, text = 'Hello').pack()
# tkinter.Button(window, text="Greet", command = greet).pack()

# Aranjare cu pack () ----------------------------

# tkinter.Label(window, text='Nume : ').pack()
# name_entry = tkinter.Entry(window)
# name_entry.pack()

# def greet():
#     name = name_entry.get()
#     tkinter.Label(window, text = f'Hello {name}').pack()

# def greet_internal():
#     name = name_entry.get()
#     print(name)

# tkinter.Button(window, text='Show', command=greet).pack()
# tkinter.Button(window, text='Show in terminal', command=greet_internal).pack()

# Aranjare cu grid () ----------------------------

# tkinter.Label(window, text='Nume : ').grid(row=0, column=0)
# name_entry = tkinter.Entry(window)
# name_entry.grid(row=0, column=1)

# output_label = tkinter.Label(window, text = '')
# output_label.grid(row = 0, column=2)

# def greet():
#     name = name_entry.get()
#     output_label.config(text = f'Hello {name}')

# tkinter.Button(window, text='Show', command=greet).grid(row=1, column=2)

# Afisare info label, text, label + stringvar, listbox ----------------------------

text_output = tkinter.Text(window, height=5, width=30)
text_output.pack()

person = tkinter.Entry(window)
person.pack()

def display_message():
    my_list=['Ionel','Dorel','Cosmin']
    text_output.delete('1.0',tkinter.END) # sterge de la inceput pana la END
    text_output.insert(tkinter.END, 'This is the list of people. Click : ')
    for elem in my_list :
        text_output.insert(tkinter.END, f'{elem}\n')

def add_person():
    person_name = person.get()
    text_output.insert(tkinter.END, f'{person_name}\n')

tkinter.Button(window, text = 'Display', command = display_message).pack()
tkinter.Button(window, text = 'Add', command = add_person).pack()



window.mainloop() # tine interfata activa pana cand o inchid eu manual