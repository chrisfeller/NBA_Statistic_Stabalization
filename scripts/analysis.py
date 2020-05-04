# Project: Statistic Stabilization
# Description: Calculate Correlation Over Time for Individual Statistics
# Data Sources: Basketball-Reference
# Last Updated: 11/8/2019

import numpy as np
import pandas as pd
import seaborn as sns
from functools import reduce
import matplotlib.pyplot as plt

# Plotting Style
plt.style.use('fivethirtyeight')

if __name__=='__main__':
    games_df = pd.read_csv('../data/games.csv')
    seasons_df = pd.read_csv('../data/seasons.csv')

    # Create SEASON field
    games_df['SEASON'] = (pd.to_datetime(games_df['Date'])
                            .map(lambda x: x.year + 1 if x.month in np.arange(10, 13, 1)
                                                      else x.year))

    # Create GAME_NUMBER field 0-82 for each team
    games_df['GAME_NUMBER'] = (games_df.sort_values(by='Date', ascending=True)
                                      .groupby(['Tm', 'SEASON']).cumcount()+1)

    # Create new df w/ cumulative statistics up to each game number
    games_df[['FG', 'FGA', '2P', '2PA', '3P', '3PA', 'FT', 'FTA']] = (games_df.sort_values(by='Date', ascending=True)
                                                        .groupby(['Tm', 'SEASON'])
                                                        [['FG', 'FGA', '2P', '2PA', '3P', '3PA', 'FT', 'FTA']]
                                                        .cumsum())
    games_df = games_df[['Date', 'Tm', 'SEASON', 'GAME_NUMBER', 'FG', 'FGA', '2P', '2PA', '3P', '3PA', 'FT', 'FTA']]

    # Calculate new metrics
    games_df['FG%'] = games_df['FG']/games_df['FGA']
    games_df['2P%'] = games_df['2P']/games_df['2PA']
    games_df['3P%'] = games_df['3P']/games_df['3PA']
    games_df['FT%'] = games_df['FT']/games_df['FTA']

    # Plot Distribution of Game-by-Game Statistics
    fig, ax = plt.subplots(figsize=(18, 5))
    sns.distplot(games_df['FG%'], kde=False)
    plt.title('Distribution of Game-by-Game FG%')
    plt.tight_layout()
    plt.show()

    fig, ax = plt.subplots(figsize=(18, 5))
    sns.distplot(games_df['2P%'], kde=False)
    plt.title('Distribution of Game-by-Game 2P%')
    plt.tight_layout()
    plt.show()

    fig, ax = plt.subplots(figsize=(18, 5))
    sns.distplot(games_df['3P%'], kde=False)
    plt.title('Distribution of Game-by-Game 3P%')
    plt.tight_layout()
    plt.show()

    fig, ax = plt.subplots(figsize=(18, 5))
    sns.distplot(games_df['FT%'], kde=False)
    plt.title('Distribution of Game-by-Game FT%')
    plt.tight_layout()
    plt.show()

    # Create Column of Season-Ending Statistic
    season_ending_df = games_df[games_df['GAME_NUMBER']==82][['Tm', 'SEASON', 'FG%', '2P%', '3P%', 'FT%']]
    season_ending_df.columns = ['Tm', 'SEASON', 'SEASON_FG%', 'SEASON_2P%', 'SEASON_3P%', 'SEASON_FT%']
    games_df = pd.merge(games_df, season_ending_df, on=['Tm', 'SEASON'], how='left')

    # Calculate Correlation between game number and season ending
    df_list = []
    for pair in [['FG%', 'SEASON_FG%'], ['2P%', 'SEASON_2P%'], ['3P%', 'SEASON_3P%'], ['FT%', 'SEASON_FT%']]:
        inner_df = games_df.groupby('GAME_NUMBER')[pair].corr().reset_index()
        inner_df = inner_df[inner_df['level_1']==pair[1]][['GAME_NUMBER', pair[0]]]
        df_list.append(inner_df)

    # Join all metrics together
    df_final = reduce(lambda left,right: pd.merge(left,right,on='GAME_NUMBER'), df_list)

    # Plot Correlation Over Time
    fig, ax = plt.subplots(figsize=(18, 5))
    sns.lineplot(x='GAME_NUMBER', y='FG%', data=df_final, label='FG%')
    sns.lineplot(x='GAME_NUMBER', y='2P%', data=df_final, label='2P%')
    sns.lineplot(x='GAME_NUMBER', y='3P%', data=df_final, label='3P%')
    sns.lineplot(x='GAME_NUMBER', y='FT%', data=df_final, label='FT%')
    ax.set_xlabel('Game Number')
    ax.set_ylabel('Correlation')
    ax.set_ylim(0.2, 1.1)
    plt.title('Correlation by Game')
    plt.tight_layout()
    plt.show()
