import PySimpleGUI as sg
import functions

list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
layout = [[sg.Text("Enter a To-Do")],
          [sg.InputText(key="todo")],
          [sg.Button('Add')],
          [list_box, edit_button]]

window = sg.Window("A TO-DO App", layout, font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            new_todo = values["todo"]
            todo_to_edit = values["todos"][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()