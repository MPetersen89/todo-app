import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme("DarkTeal6")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button(size=4, image_source="add.png", mouseover_colors="dark green",
                       tooltip="Add to-do", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="complete.png", mouseover_colors="dark green",
                            tooltip="Complete to-do", key="Complete")
exit_button = sg.Button("Exit")

col1 = sg.Column([[edit_button], [complete_button]])

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, col1],
                           [exit_button]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do to edit.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select a to-do to complete.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()




