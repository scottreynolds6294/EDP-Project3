import pandas as pd
import numpy as np

data = pd.read_csv('troop_movements.csv')

data['is_resistance'] = data['empire_or_resistance'].str.lower() == 'resistance'

print(data[['empire_or_resistance', 'is_resistance']].head())