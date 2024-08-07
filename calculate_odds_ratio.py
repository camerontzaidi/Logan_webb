import pandas as pd
from pybaseball import statcast_pitcher, playerid_lookup
import scipy.stats as stats

def get_player_id(first_name, last_name):
    player_info = playerid_lookup(last_name, first_name)
    return player_info['key_mlbam'].values[0]

def calculate_odds_ratios(start_year, end_year, player_id):
    results_df = pd.DataFrame()

    for year in range(start_year, end_year + 1):
        data = statcast_pitcher(start_dt=f'{year}-01-01', end_dt=f'{year}-12-31', player_id=player_id)
        hit_data = data[data['events'].isin(['single', 'double', 'triple', 'home_run'])]
        hit_counts = hit_data['pitch_type'].value_counts()
        pitch_counts = data['pitch_type'].value_counts()

        results_season = {'Pitch_Type': [], 'Odds_Ratio': [], 'P_Value': []}
        for pitch_type in pitch_counts.index:
            hit_given_pitch = hit_counts.get(pitch_type, 0)
            hit_given_other = hit_counts.sum() - hit_given_pitch
            pitch_given_pitch = pitch_counts.get(pitch_type, 0)
            pitch_given_other = pitch_counts.sum() - pitch_given_pitch

            odds_ratio = (hit_given_pitch / pitch_given_pitch) / (hit_given_other / pitch_given_other)
            contingency_table = [[hit_given_pitch, hit_given_other], [pitch_given_pitch, pitch_given_other]]
            _, p_value = stats.fisher_exact(contingency_table)

            results_season['Pitch_Type'].append(pitch_type)
            results_season['Odds_Ratio'].append(odds_ratio)
            results_season['P_Value'].append(p_value)

        season_df = pd.DataFrame(results_season)
        results_df = pd.concat([results_df, season_df], axis=1)

    return results_df

if __name__ == "__main__":
    first_name = "Logan"
    last_name = "Webb"
    player_id = get_player_id(first_name, last_name)
    start_year = 2019
    end_year = 2024

    odds_ratios_df = calculate_odds_ratios(start_year, end_year, player_id)
    odds_ratios_df.to_csv('data/logan_webb_odds_ratios.csv', index=False)
