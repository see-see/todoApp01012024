import PySimpleGUI as sg
import functions as f

input_box = sg.InputText(key="todo", size=30)
list_box = sg.Listbox(f.readfile(), size=(20, 10), key='list',
                      expand_x=True, enable_events=True)
add = sg.Button("Add todo", key="add")

edit = sg.Button("Edit", key="edit", disabled=(True if not f.readfile() else
                                               False))
complete = sg.Button("Complete", key="comp", disabled=(True if not f.readfile() else
                                               False))
layout = [
    [sg.Text("Add todo")],
    [input_box, add],
    [list_box, edit, complete]
]

window = sg.Window(title="Hello", layout=layout)
while True:
    event, values = window.read()

    if event == 'add':
        if values['todo']:
            todo = f.readfile()
            todo.append(values['todo'] + '\n')
            f.writefile(todo)
            window['list'].update(values=f.readfile())
        else:
            sg.popup_ok("Enter a todo!")

    elif event == 'list':
        if values['list']:
            window['edit'].update(disabled=False)
            window['comp'].update(disabled=False)
            window['todo'].update(value=str(values['list'][0]).strip())

    elif event == 'edit':
        if not values['list']:
            sg.popup_ok("Select a todo from the list!")
        elif values['todo']:
            todo = f.readfile()
            text = values['list'][0]
            position = todo.index(text)
            todo[position] = values['todo'] + '\n'
            f.writefile(todo)
            window['list'].update(values=f.readfile())
        else:
            sg.popup_ok("Enter a todo!")

    elif event == 'comp':
        if not values['list']:
            sg.popup_ok("Select a todo from the list!")
        else:
            todo = f.readfile()
            text = values['list'][0]
            todo.pop(todo.index(text))
            f.writefile(todo)
            window['list'].update(values=f.readfile())
            window['todo'].update("")
            if not f.readfile():
                window['edit'].update(disabled=True)
                window['comp'].update(disabled=True)

    elif event == sg.WINDOW_CLOSED:
        break

    print(event, values)