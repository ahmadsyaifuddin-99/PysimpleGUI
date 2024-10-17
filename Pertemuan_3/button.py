import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#ffff00")
window = sg.Window(title="Contoh Button",
                layout=[[sg.Text("Contoh Button")],
                        [sg.Button("Simpan")],
                        [sg.Button("Keluar")]
                        ],
                        size=(400,200),
                        font=("Times",18))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()
                        