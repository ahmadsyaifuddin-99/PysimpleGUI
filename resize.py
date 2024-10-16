import PySimpleGUI as sg
susunan=[[sg.Text("UNISKA MAB",font=("Helvetica",24))],
         [sg.Text("BANJARMASIN", font=("Courier",18))]]
window = sg.Window(title="New Icon",
                   layout=susunan,
                   element_justification= "center",
                   icon="favicon.ico",
                   resizable=True,
                   size=(430,200))
window.read()
window.close()