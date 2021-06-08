import json
import numpy as np
import pandas as pd
from datetime import date
from joblib import load
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
from functools import partial
from Shot import Player, Shot
from Draw_HS_Court import draw_HS_court
from Player_Entry import player_entry, submit_teams

def data_entry():
    root = Tk()
    # root.geometry("584x643")
    # root.resizable(width=False, height=False)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    global fig, ax, circle
    global home_points, away_points, home_shots, away_shots, shot_index, home_team, away_team, home_list, away_list

    home_points = 0
    away_points = 0
    home_shots = 0
    away_shots = 0
    shot_index = 0
    List = []

    team_label_font = tkFont.Font(family='Helvetica', size=20, weight='bold')
    team_entry_font = tkFont.Font(family='Hevetica', size=15)
    button_font = tkFont.Font(family='Hevetica', size=12)
    reg_font = tkFont.Font(family='Hevetica', size=12)


    team_frame = LabelFrame(root, padx=10, pady=10)
    team_frame.pack(side=TOP, padx=10, pady=10)

    home_label = Label(team_frame, text="Home", font=team_label_font)
    away_label = Label(team_frame, text="Away", font=team_label_font)

    home_label.grid(row=0, column=0, sticky=N+S+E+W)
    away_label.grid(row=0, column=3, sticky=N+S+E+W)

    home_name_label = Label(team_frame, text=home_team, font=team_entry_font)
    away_name_label = Label(team_frame, text=away_team, font=team_entry_font)
    home_name_label.grid(row=1, column=0, padx=(0,20)) # sticky=N+S+E+W)
    away_name_label.grid(row=1, column=3, padx=(20,0)) #, sticky=N+S+E+W)

    button_frame = LabelFrame(root)
    button_frame.pack(padx=10, pady=10)
    button1 = Button(button_frame, text='Show Pitch', command=draw_court, font=button_font)
    button1.pack(padx=(5, 50), pady=5, side=LEFT)

    save_file_button = Button(button_frame, text='Save Data as .CSV', command=saveCSV, font=button_font)
    save_file_button.pack(padx=(50,5), pady=5, side=RIGHT)

    outer = LabelFrame(root)
    outer.pack(padx=10, pady=10)

    key = LabelFrame(outer, text="Key", font=reg_font)
    key.pack(side=LEFT)
    key_text1 = Label(key, text="Shot Made: LClick (Orange)", font=reg_font)
    key_text2 = Label(key, text="Shot Missed: RClick (Blue)", font=reg_font)
    key_text1.pack(fill=BOTH, expand=YES)
    key_text2.pack(fill=BOTH, expand=YES)

    scoreboard = LabelFrame(outer, text="Game Scoreboard", font=reg_font)
    scoreboard.pack(side=RIGHT)
    scoreboard_home = Label(scoreboard, text="Home", font=reg_font)
    scoreboard_away = Label(scoreboard, text="Away", font=reg_font)
    shots_label = Label(scoreboard, text="Shots: ", font=reg_font)
    score_frame1 = LabelFrame(scoreboard)
    score_frame2 = LabelFrame(scoreboard)
    score_home_label = Label(score_frame1, text=str(home_goals), font=reg_font)
    score_away_label = Label(score_frame2, text=str(away_goals), font=reg_font)
    shots_home_label = Label(scoreboard, text=str(home_shots), font=reg_font)
    shots_away_label = Label(scoreboard, text=str(away_shots), font=reg_font)
    SOT_label = Label(scoreboard, text="SOT: ", font=reg_font)
    SOT_home_label = Label(scoreboard, text=str(home_SOT), font=reg_font)
    SOT_away_label = Label(scoreboard, text=str(away_SOT), font=reg_font)
    scoreboard_home.grid(row=0, column=1)
    scoreboard_away.grid(row=0, column=2)
    score_frame1.grid(row=1, column=1)
    score_frame2.grid(row=1, column=2)
    score_home_label.pack()
    score_away_label.pack()
    shots_label.grid(row=2, column=0)
    shots_home_label.grid(row=2, column=1)
    shots_away_label.grid(row=2, column=2)
    SOT_label.grid(row=3, column=0)
    SOT_home_label.grid(row=3, column=1)
    SOT_away_label.grid(row=3, column=2)
    
    root.mainloop()
    
    
if __name__ == '__main__':
    home_team, away_team, home_list, away_list = player_entry()
    data_entry()
    