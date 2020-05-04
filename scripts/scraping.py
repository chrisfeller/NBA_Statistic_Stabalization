# Project: Statistic Stabilization
# Description: Scrape Team/Game data for last 10 seasons
# Data Sources: Basketball-Reference
# Last Updated: 11/7/2019

import numpy as np
import pandas as pd
from time import sleep


def game_scraper(save=False):
    # Link to game-finder on Basketball-Reference
    url = """https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&player=&match=game&lg_id=NBA&year_min=2010&year_max=2019&team_id=&opp_id=&is_range=N&is_playoffs=N&round_id=&best_of=&team_seed=&opp_seed=&team_seed_cmp=eq&opp_seed_cmp=eq&game_num_type=team&game_num_min=&game_num_max=&game_month=&game_location=&game_result=&is_overtime=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=date_game&order_by_asc=&offset={0}"""
    # Placeholder dataframe to append individual page results to
    df = pd.DataFrame()
    # Loop through individual pages on Basketball-Reference
    for page in np.arange(0, 24500, 100):
        print(page)
        try:
            # Read in table
            table = pd.read_html(url.format(page))[0]
            # Drop multi-index
            table.columns = table.columns.droplevel()
            # Remove headers within table
            table = table[table["Tm"] != "Tm"]
            # Keep only team stats' exlude opponent stats
            table = table.iloc[:, 0:20]
            # Append individual page to overall results
            df = df.append(table, sort=False)
        except:
            pass
    # Update team names
    team_dict = {"NOH": "NOP", "NJN": "BRK", "CHO": "CHA"}
    df.replace({"Tm": team_dict}, inplace=True)
    # Save dataframe if `save` parameter is set to True
    if save:
        df.to_csv("../data/games.csv", index=False)
    else:
        return df


def season_scraper(save=False):
    # Link to season-finder on Basketball-Reference
    url = """https://www.basketball-reference.com/play-index/tgl_finder.cgi?request=1&player=&match=single&lg_id=NBA&year_min=2010&year_max=2019&team_id=&opp_id=&is_range=N&is_playoffs=N&round_id=&best_of=&team_seed=&opp_seed=&team_seed_cmp=eq&opp_seed_cmp=eq&game_num_type=team&game_num_min=&game_num_max=&game_month=&game_location=&game_result=&is_overtime=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=date_game&order_by_asc=&offset={0}"""
    # Placeholder dataframe to append individual page results to
    df = pd.DataFrame()
    # Loop through individual pages on Basketball-Reference
    for page in np.arange(0, 400, 100):
        try:
            # Read in table
            table = pd.read_html(url.format(page))[0]
            # Drop multi-index
            table.columns = table.columns.droplevel()
            # Remove headers within table
            table = table[table["Tm"] != "Tm"]
            # Keep only team stats' exlude opponent stats
            table = table.iloc[:, 0:21]
            # Append individual page to overall results
            df = df.append(table, sort=False)
        except:
            pass
    # Update team names
    team_dict = {"NOH": "NOP", "NJN": "BRK", "CHO": "CHA"}
    df.replace({"Tm": team_dict}, inplace=True)
    # Save dataframe if `save` parameter is set to True
    if save:
        df.to_csv("../data/seasons.csv", index=False)
    else:
        return df


def player_scraper(save=False):
    url = """https://www.basketball-reference.com/play-index/pgl_finder.cgi?request=1&player_id=&match=game&year_min=2015&year_max=2019&age_min=0&age_max=99&team_id=&opp_id=&season_start=1&season_end=-1&is_playoffs=N&draft_year=&round_id=&game_num_type=&game_num_min=&game_num_max=&game_month=&game_day=&game_location=&game_result=&is_starter=&is_active=&is_hof=&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&c1stat=&c1comp=&c1val=&c1val_orig=&c2stat=&c2comp=&c2val=&c2val_orig=&c3stat=&c3comp=&c3val=&c3val_orig=&c4stat=&c4comp=&c4val=&c4val_orig=&is_dbl_dbl=&is_trp_dbl=&order_by=date_game&order_by_asc=Y&offset={0}"""
    df = pd.DataFrame()
    for page in np.arange(0, 135000, 100):
        print(page)
        try:
            table = pd.read_html(url.format(page))[0]
            table = table[table["Player"] != "Player"]
            df = df.append(table, sort=False)
        except:
            pass
    if save:
        df.to_csv("../data/players.csv", index=False)
    else:
        return df


if __name__ == "__main__":
    # Scrape Data
    # game_scraper(save=True)
    # season_scraper(save=True)
    # player_scraper(save=True)
