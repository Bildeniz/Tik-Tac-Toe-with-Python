import tkinter as tk
from tkinter import messagebox
from playsound import playsound
from threading import Thread

whose_turn = 'X'

def button_listener(row, col, buttons, whose_turn_label):
    global whose_turn
    if ''  == buttons[row][col].cget('text'):
        
        button = buttons[row][col]
        button.config(text=whose_turn)

        if whose_turn == 'X':
            button.config(fg='red')
        else:
            button.config(fg='light blue')


        if whose_turn == 'X':
            whose_turn = 'O'
            whose_turn_label.config(text='O', fg='light blue')
        else:
            whose_turn = 'X'
            whose_turn_label.config(text='X', fg='red')
    
        result = check_all_combo(get_button_texts(buttons))
        
        if not result== 0:
            play_sound_asyn('game.mp3')
            messagebox.showinfo('Tic-Tac-Toe', f'{result} KAZANDI!!!!!!!!!!!!!!!')

            reset(buttons, whose_turn_label)

        if check_is_it_full(get_button_texts(buttons)) == 1:
            play_sound_asyn('reset.mp3')
            messagebox.showerror('Tic-Tac-Toe', 'Hamle kalmadı!')
            reset(buttons, whose_turn_label)

def reset(buttons, whose_turn_label):
    global whose_turn
    for row in buttons:
        for button in row:
            button.config(text='')

    whose_turn = 'X'
    whose_turn_label.config(text='X', fg='red')

        
def get_button_texts(buttons:list) -> list:
    buttons_label = []
    
    for row in buttons:
        row_labels = []
        for button in row:
            row_labels.append(button.cget('text'))
    
        buttons_label.append(row_labels)
    return buttons_label

def check_all_combo(buttons_label):
    get_all_rows = buttons_label
    get_all_columns = [[row[0] for row in buttons_label], [row[1] for row in buttons_label], [row[2] for row in buttons_label]]
    get_all_diagonals = [[buttons_label[0][0], buttons_label[1][1], buttons_label[2][2]], [buttons_label[0][2], buttons_label[1][1], buttons_label[2][0]]]

    all_combos=get_all_rows+get_all_columns+get_all_diagonals

    for combo in all_combos:
        if how_many(combo, 'O') == 3:
            return 'O'
        elif how_many(combo, 'X') == 3:
            return 'X'

    return 0

def check_is_it_full(buttons_label):
    x=0
    o=0
    for row in buttons_label:
        for col in row:
            x = x + how_many(col, 'X')
            o = o + how_many(col, 'O')
    if x+o == 9:
        return 1
    else:
        return 0

def how_many(list_to_check, item_to_find):
    number = 0
    for value in list_to_check:
        if value == item_to_find:
            number+=1
    return number

def play_sound(sound):
    playsound('sounds\\'+sound)

def play_sound_asyn(sound):
    Thread(target=lambda sound=sound: play_sound(sound)).start()
