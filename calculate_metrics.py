import pandas as pd

data = pd.read_csv('data/logan_webb_data.csv')
data['game_date'] = pd.to_datetime(data['game_date'])
data['strikeouts'] = (data['description'] == 'strikeout').astype(int)
data['walks'] = (data['description'] == 'walk').astype(int)
data['home_runs'] = (data['events'] == 'home_run').astype(int)
data['pop_ups'] = (data['launch_angle'] > 50).astype(int)
data['fly_balls'] = ((data['launch_angle'] > 25) & (data['launch_angle'] <= 50)).astype(int)
data['ground_balls'] = ((data['launch_angle'] > -25) & (data['launch_angle'] <= 25)).astype(int)
data['swinging_strikes'] = data['description'].str.contains('swinging').astype(int)

rates = data.groupby(data['game_date'].dt.year).agg(
    strikeouts_per_game=('strikeouts', 'mean'),
    walks_per_game=('walks', 'mean'),
    home_runs_per_game=('home_runs', 'mean'),
    pop_ups_per_game=('pop_ups', 'mean'),
    fly_balls_per_game=('fly_balls', 'mean'),
    ground_balls_per_game=('ground_balls', 'mean'),
    swinging_strikes_per_game=('swinging_strikes', 'mean')
)

rates.to_csv('data/logan_webb_metrics.csv')
