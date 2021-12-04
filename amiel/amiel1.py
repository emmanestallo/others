import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sp 
import pandas as pd 

def get_elo(i):
    team_1 = df.iloc[i]['Visitor/Neutral']
    team_2 = df.iloc[i]['Home/Neutral'] 
    MOV = abs(df.iloc[i]['PTS'] - df.iloc[i]['PTS.1']) 
    k = 20*(((MOV+3)**(0.8))/(7.5+0.006*abs(home[team_2]-road[team_1])))
    #home ea calculation 
    home_ea = 1/(1+(10**(road[team_1]/400-home[team_2]/400))) 

    #road ea calculation 
    road_ea = 1/(1+(10**(home[team_2]/400-road[team_1]/400))) 

    #s calculation 
    if df.iloc[i]['PTS.1'] - df.iloc[i]['PTS'] > 0:
        s_home = 1   
        s_road = 0 
    else: 
        s_home = 0 
        s_road = 1 

    #home elo calculation 
    home[team_2] = k*(s_home-home_ea) + home[team_2] 

    #road elo calculation 
    road[team_1] = k*(s_road-road_ea) + road[team_1]

teams = []

df = pd.read_csv('NBA-2010-2011-SCHEDULE.csv')
df.dropna(how='all', axis=1, inplace=True)

home = {}
road = {}

for i in df['Visitor/Neutral']: 
    home[i] = 1300
for j in df['Home/Neutral']:
    road[j] = 1300

for team in home: 
    teams.append(team) 

for team in road: 
    if team not in teams: 
        teams.append(team)

for i in range(len(df)):
    get_elo(i)

for i in teams:
    print(f'{i}: Home Elo = {round(home[i],4)}, Road Elo = {round(road[i],4)}')


