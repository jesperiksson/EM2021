#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 14:47:42 2021

@author: jesper
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import resultat

goal_filter = 5 # Om ett lag gjort fler än 5 mål räknas bara 5

class Team_stats():
    def __init__(self,name):
        self.name = name
        self.avg_scored = 0
        self.avg_conceded = 0
        self.n_games = 0
        self.df = pd.DataFrame(columns=['s','c'])
        
    def add_game(self,s,c):
        self.avg_scored = (self.avg_scored * self.n_games + min(s,goal_filter))/(self.n_games+1)
        self.avg_conceded = (self.avg_conceded * self.n_games + min(c,goal_filter))/(self.n_games+1)
        self.n_games += 1
        
#group_a = pd.DataFrame(columns=['Italien','Turkiet','Wales','Schweiz'])

#%%

def add_stats(stats,results):
    for index, game  in results.iterrows():
        stats.add_game(game['gjorda'],game['insläppta'])
        
def simulate_game(team1,team2):
    mu_team1_score = team1.avg_scored
    mu_team1_concede = team1.avg_conceded
    mu_team2_score = team2.avg_scored
    mu_team2_concede = team2.avg_conceded
    result = [np.random.poisson((mu_team1_score+mu_team2_concede)/2),
              np.random.poisson((mu_team1_concede+mu_team2_score)/2)]
    return result

def simulate_games(team1,team2,n_games):
    cols =[team1.name,team2.name]
    results = pd.DataFrame(columns=cols)
    for i in range(n_games):
        results = results.append(pd.DataFrame([simulate_game(team1,team2)],columns=cols))
        #print(results)
    return results        

#%% Grupp B
danmark_stats = Team_stats('danmark')
finland_stats = Team_stats('finland')
ryssland_stats = Team_stats('ryssland')
belgien_stats = Team_stats('belgien')

add_stats(danmark_stats,resultat.danmark)
add_stats(finland_stats,resultat.finland)
add_stats(ryssland_stats,resultat.ryssland)
add_stats(belgien_stats,resultat.belgien)

#results = simulate_games(danmark_stats,finland_stats,1000)
#%%
def plot_result_hist(results,team1,team2):
    plt.hist(results[team1],bins=np.arange(max(results[team2])+3)-0.5,alpha=0.75,color='red' ,label=team1)
    plt.hist(results[team2],bins=np.arange(max(results[team2])+3)-0.5,alpha=0.75,color='blue',label=team2)
    plt.legend()
    plt.show()

#%%
bel_rus = simulate_games(belgien_stats,ryssland_stats,10000)
plot_result_hist(bel_rus,'belgien','ryssland')




