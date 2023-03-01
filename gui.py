import PySimpleGUI as sg


layout = [[sg.Text("Enter a To-Do")],
          [sg.InputText()],
          [sg.Button('Add')] ]

window = sg.Window("A TO-DO App", layout)

event, values = window.read()

print("hello", values[0], "Does this works?")

window.close()