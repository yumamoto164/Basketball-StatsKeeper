import json
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date
from joblib import load
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import ginput
from matplotlib.patches import Arc
from matplotlib.widgets import Cursor
from functools import partial
from Draw_NBA_Court import draw_NBA_court
from Draw_College_Court import draw_college_court
from Draw_HS_Court import draw_HS_court
from Player_Entry import player_entry, submit_teams
from Shot import Player, Shot

def draw_court():
    global fig, ax
    fig, ax = draw_HS_court()
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.ion()
    plt.show()
    
# def isInside():
    
    

def onclick(event):
    global home_points, away_points, home_shots, away_shots, shot_index, fig, ax
    x_loc = round(event.xdata,2)
    y_loc = round(event.ydata,2)
    
    if team_button1.pressed:
        team = "Home"
        team_name = home_team
        if(home_dropdown.get() == ''):
            shot_output.config(text='Please Choose a Player for the Shot', foreground="red")
            return
        split = home_dropdown.get().split("--")
        player_name = split[1]
        player_number = int(split[0])
        home_shots += 1
        shots_home_label.configure(text=str(home_shots))
    else:
        team = "Away"
        team_name = away_team
        if(away_dropdown.get() == ''):
            shot_output.config(text='Please Choose a Player for the Shot', foreground="red")
            return
        split = away_dropdown.get().split("--")
        player_name = split[1]
        player_number = int(split[0])
        away_shots += 1
        shots_away_label.configure(text=str(away_shots))
    
    # Contested/Not Contested
    if contested_button.pressed:
        contested = True
    else:
        contested = False
        
    if str(event.button) == "MouseButton.LEFT":
        make = True
        circle = plt.Circle((x_loc, y_loc), 0.75, color='red')
    elif str(event.button) == "MouseButton.RIGHT":
        make = False
        circle = plt.Circle((x_loc, y_loc), 0.75, color='blue')
        
    new_shot = Shot(shot_index, team_name, player_name, player_number, make, x_loc, y_loc, contested)
    ax.add_artist(circle)
    plt.draw()
    

class TeamButton():
    def __init__(self, input_text, text_font, data_entry):
        self.input_text = input_text
        self.text_font = text_font
        self.data_entry = data_entry
        if self.input_text == "Home":
            self.pressed = True
            self.button = Button(self.data_entry, text=input_text, command=self.updateHome, relief=SUNKEN, font=self.text_font)
        else:
            self.pressed = False
            self.button = Button(self.data_entry, text=input_text, command=self.updateAway, relief=RAISED, font=self.text_font)
    
    def updateHome(self):
        if self.pressed == False:
            self.button.configure(relief=SUNKEN)
            team_button2.button.configure(relief=RAISED)
            self.pressed = True
            team_button2.pressed = False
        
    def updateAway(self):
        if self.pressed == False:
            self.button.configure(relief=SUNKEN)
            team_button1.button.configure(relief=RAISED)
            self.pressed = True
            team_button1.pressed = False
            
            
class  ContestedButton():
    def __init__(self, input_text, text_font, data_entry):
        self.input_text = input_text
        self.text_font = text_font
        self.data_entry = data_entry
        if self.input_text == "Contested":
            self.pressed = True
            self.button = Button(self.data_entry, text=input_text, command=self.updateContested, relief=SUNKEN, font=self.text_font)
        else:
            self.pressed = False
            self.button = Button(self.data_entry, text=input_text, command=self.updateNotContested, relief=RAISED, font=self.text_font)
    
    def updateContested(self):
        if self.pressed == False:
            self.button.configure(relief=SUNKEN)
            notcontested_button.button.configure(relief=RAISED)
            self.pressed = True
            notcontested_button.pressed = False
        
    def updateNotContested(self):
        if self.pressed == False:
            self.button.configure(relief=SUNKEN)
            contested_button.button.configure(relief=RAISED)
            self.pressed = True
            contested_button.pressed = False
            
            
def removeLast():
    global home_points, away_points, home_shots, away_shots, shot_index
    if len(List) != 0:
        circle.remove()
        removed_shot = List.pop()
        
        if removed_shot['Team'] == home_team:
            if removed_shot['Make'] == 1:
                home_points -= 1
                score_home_label.configure(text=str(home_points))
            if removed_shot['onTarget'] == 1:
                home_SOT -= 1
                SOT_home_label.configure(text=str(home_SOT))
            home_shots -= 1
            shots_home_label.configure(text=str(home_shots))
        else:
            if removed_shot['isGoal'] == 1:
                away_points -= 1
                score_away_label.configure(text=str(away_points))
            if removed_shot['onTarget'] == 1:
                away_SOT -= 1
                SOT_away_label.configure(text=str(away_SOT))
            away_shots -= 1
            shots_away_label.configure(text=str(away_shots))
        shot_index -= 1

def saveCSV():
    # save all the data in placeholders to a csv/excel file
    today = date.today()
    today = today.strftime("%b-%d-%Y")
    df = pd.DataFrame(List)
    boolean_cat = {0: False, 1: True}
    df.Make.replace(boolean_cat, inplace=True)
    home_team_underscore = home_team.replace(" ", "_")
    away_team_underscore = away_team.replace(" ", "_")
    df.to_csv(f'output/csv_files/{home_team_underscore}_vs_{away_team_underscore}{today}.csv')

if __name__ == '__main__':
    home_team, away_team, home_list, away_list = player_entry()
    
    root = Tk()
    # root.geometry("584x643")
    # root.resizable(width=False, height=False)
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)

    global fig, ax, circle
    global home_points, away_points, home_shots, away_shots, shot_index

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
    button1 = Button(button_frame, text='Show Court', command=draw_court, font=button_font)
    button1.pack(padx=(5, 50), pady=5, side=LEFT)

    save_file_button = Button(button_frame, text='Save Data as .CSV', command=saveCSV, font=button_font)
    save_file_button.pack(padx=(50,5), pady=5, side=RIGHT)

    outer = LabelFrame(root)
    outer.pack(padx=10, pady=10)

    key = LabelFrame(outer, text="Key", font=reg_font)
    key.pack(side=LEFT)
    key_text1 = Label(key, text="Shot Made: LClick (Red)", font=reg_font)
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
    score_home_label = Label(score_frame1, text=str(home_points), font=reg_font)
    score_away_label = Label(score_frame2, text=str(away_points), font=reg_font)
    shots_home_label = Label(scoreboard, text=str(home_shots), font=reg_font)
    shots_away_label = Label(scoreboard, text=str(away_shots), font=reg_font)
    
    scoreboard_home.grid(row=0, column=1)
    scoreboard_away.grid(row=0, column=2)
    score_frame1.grid(row=1, column=1)
    score_frame2.grid(row=1, column=2)
    score_home_label.pack()
    score_away_label.pack()
    shots_label.grid(row=2, column=0)
    shots_home_label.grid(row=2, column=1)
    shots_away_label.grid(row=2, column=2)
    
    data_entry = LabelFrame(root, text="Record Shots", padx=10, font=reg_font)
    data_entry.pack(padx=10, pady=10)

    team = Label(data_entry, text="Team: ", font=reg_font)
    team_button1 = TeamButton("Home", button_font, data_entry)
    team_button2 = TeamButton("Away", button_font, data_entry)
    contested = Label(data_entry, text="Contested: ", font=reg_font)
    contested_button = ContestedButton("Contested", button_font, data_entry)
    notcontested_button = ContestedButton("Not Contested", button_font, data_entry)
    home_dropdown_label = Label(data_entry, text="Home Player: ", font=reg_font)
    away_dropdown_label = Label(data_entry, text="Away Player: ", font=reg_font)
    home_dropdown_values = list(str(player.getNumber()) + "--" + player.getName() for player in home_list)
    away_dropdown_values = list(str(player.getNumber()) + "--" + player.getName() for player in away_list)
    home_dropdown = ttk.Combobox(data_entry, width=20, values=home_dropdown_values)
    away_dropdown = ttk.Combobox(data_entry, width=20, values=away_dropdown_values)
    shot_output = Label(data_entry, text="Output", font=reg_font)
    remove_last_button = Button(root, text='Remove Last Entry', command=removeLast, font=button_font)
    
    team.grid(row=0, column=0)
    team_button1.button.grid(row=0, column=1, padx=5, pady=5)
    team_button2.button.grid(row=0, column=2, padx=5, pady=5)
    contested.grid(row=1, column=0)
    contested_button.button.grid(row=1, column=1, padx=5, pady=5)
    notcontested_button.button.grid(row=1, column=2, padx=5, pady=5)
    home_dropdown_label.grid(row=2, column=0, padx=5, pady=5)
    home_dropdown.grid(row=2, column=1, padx=(5,10), pady=5)
    away_dropdown_label.grid(row=2, column=2, padx=(10,5), pady=5)
    away_dropdown.grid(row=2, column=3, padx=5, pady=5)
    home_dropdown.current()
    away_dropdown.current()
    shot_output.grid(row=3, column=2)
    remove_last_button.pack()
    
    root.mainloop()