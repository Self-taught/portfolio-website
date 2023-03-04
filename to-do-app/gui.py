import PySimpleGUI as sg
import functions
import time

clock = sg.Text("", key="clock")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
clear_button = sg.Button("Clear")
layout = [[clock],
          [sg.Text("Enter a To-Do")],
          [sg.InputText(key="todo"),
           sg.Button(size=1, image_source="add.png", mouseover_colors="LightBlue", tooltip="Add todo", key="Add"), clear_button],
          [list_box, edit_button, complete_button]]

window = sg.Window("A TO-DO App", layout, font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=10000)
    window["clock"].update(value=time.strftime("%b %d %Y %M %H %M"))
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
            try:
                new_todo = values["todo"]
                todo_to_edit = values["todos"][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Select an item first!", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Select an item first!", font=("Helvetica", 20))
        case "Clear":
            window["todo"].update(value="")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()