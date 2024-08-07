### scripts/get_data.py

```python
from pybaseball import statcast_pitcher, playerid_lookup
import pandas as pd

def get_player_id(first_name, last_name):
    player_info = playerid_lookup(last_name, first_name)
    return player_info['key_mlbam'].values[0]

def main():
    first_name = "Logan"
    last_name = "Webb"
    player_id = get_player_id(first_name, last_name)
    data = statcast_pitcher(start_dt='2019-01-01', end_dt='2024-12-31', player_id=player_id)
    data.to_csv('data/logan_webb_data.csv', index=False)

if __name__ == "__main__":
    main()
