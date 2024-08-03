import functions
import FreeSimpleGUI as fsg
import time

clock = fsg.Text("",key="clock")
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key="New-Todo")
add_button = fsg.Button("Add")
edit_button = fsg.Button("Edit")
list_box = fsg.Listbox(values=functions.get_todos(),key="todos",
                       enable_events=True,size=[45,10])
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")
layout = [[clock],
          [label],
          [input_box,add_button],
          [list_box,edit_button,complete_button,exit_button]]
window = fsg.Window("My To-do App",
                    layout=layout,font="Verdana")

while True:
    event, values = window.read(timeout = 1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event,values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['New-Todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "Edit":
         try:
            todo_to_edit = values['todos'][0]
            new_todo = values['New-Todo'] + '\n'
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
         except IndexError:
             fsg.popup("Please select item first",title="Popup", font="verdana")

    elif event  == 'todos':
        #print("Here")
        window['New-Todo'].update(value = values['todos'][0])
    elif event == "Complete":
        #print("Here")
        try:
            complete_item = values['todos'][0]
            todos = functions.get_todos()
            #index = todos.index(complete_item)
            #todos[index] = new_todo
            todos.remove(complete_item)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['New-Todo'].update(value='')
        except IndexError:
            fsg.popup("Please select item first", title="Popup", font="verdana")
            #print(complete_item)
    elif event == "Exit":
        exit()
    if event == fsg.WIN_CLOSED:
        break

window.close()