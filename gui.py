import PySimpleGUI as sg

input_box = sg.InputText(key="todo")
add = sg.Button("Add todo", key="add")
layout = [
    [sg.Text("Add todo"), input_box, add]
]

window = sg.Window(title="Hello", layout=layout)
while True:
    events, values = window.read()

    if events == sg.WINDOW_CLOSED:
        break

    print(events, values)