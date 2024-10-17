import PySimpleGUI as sg
# sg.main()
sg.theme("DarkRed")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",

layout=[[sg.Text("SELAMAT DATANG",

font=("Courier",25))],

[sg.Text("NPM : 2210010111 ")],
[sg.Text("Nama : Ahmad Syaifuddin ")],
[sg.Text("Kelas : 5E Regular Banjarmasin ")],
[sg.Text("Matkul : Pemrograman Visual 3 ")],
],

size=(450,250),
resizable= True,
font=("Times", 18))

window()
window.close()