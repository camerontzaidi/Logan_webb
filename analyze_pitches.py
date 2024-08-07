import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/logan_webb_data.csv')

custom_colors = {
    'CH': 'orange',
    'FF': 'red',
    'SI': 'blue',
    'ST': 'green',
    'FC': 'purple'
}

data['is_strike'] = data['description'].str.contains('called_strike|swinging_strike|foul')
data['season'] = pd.to_datetime(data['game_date']).dt.year
strike_percentage_by_pitch_by_season = data.groupby(['season', 'pitch_type'])['is_strike'].mean().unstack()

plt.figure(figsize=(12, 8))
for pitch_type in strike_percentage_by_pitch_by_season.columns:
    plt.plot(strike_percentage_by_pitch_by_season.index, strike_percentage_by_pitch_by_season[pitch_type],
             label=pitch_type, color=custom_colors.get(pitch_type, 'black'))

plt.title('Strike Percentage by Pitch by Season for Logan Webb (2019-2024)')
plt.xlabel('Season')
plt.ylabel('Strike Percentage')
plt.legend(title='Pitch Type', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
