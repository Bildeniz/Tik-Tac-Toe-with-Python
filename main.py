import tkinter as tk
from func import *

root = tk.Tk()
root.title('Tic-Tac-Toe')
root.geometry('800x800')
root.resizable(0,0)
menubar = tk.Menu(root)
root.config(bg='dark gray', menu=menubar)

whose_turn_label = tk.Label(root, text=whose_turn ,font=('Calibri', 30, 'bold'), fg='red', bg='dark gray')
whose_turn_label.place(relx=0.182, rely=0.05, anchor='center')
title = tk.Label(root, text="'in sırası lütfen bir hamle yap" ,font=('Calibri', 30, 'bold'), bg='dark gray')
title.place(relx=0.5, rely=0.05, anchor='center')

frame = tk.Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, anchor='center')

buttons = []
for row in range(3):
    row_list = []
    for col in range(3):
        button = tk.Button(
        master=frame,
        text="",
        font=('Calibri', 36, "bold"),
        fg="black",
        width=5,
        height=2,
        highlightbackground="lightblue",)
        button.config(command=lambda row=row, col=col: button_listener(row, col, buttons, whose_turn_label))

        button.grid(column=col, row=row, padx=10, pady=10)
        row_list.append(button)
    buttons.append(row_list)

options_menu = tk.Menu(menubar)
options_menu.add_command(label='Sıfırla', command=lambda buttons=buttons, whose_turn_label=whose_turn_label: reset(buttons, whose_turn_label))
menubar.add_cascade(label='Seçenekler', menu=options_menu, underline=0)

root.mainloop()