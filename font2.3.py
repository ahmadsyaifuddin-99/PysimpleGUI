import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",

layout=[[sg.Text("FTI UNISKA",font=("Helvetica",24))],

[sg.Text("FAKULTAS TEKNOLOGI INFORMASI",font=("Courier",18,"italic","bold","underline"))],

[sg.Text("UNISKA MAB BANJARMASIN")]],

size=(430,200),
font=("Times", 18))

window()
window.close()