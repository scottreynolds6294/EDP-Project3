import pandas as pd
import numpy as np

data = pd.read_csv('troop_movements.csv')

empire_count = np.sum(data['empire_or_resistance'] == 'empire')
resistance_count = np.sum(data['empire_or_resistance'] == 'resistance')

counts_df = pd.DataFrame({
    'empire_or_resistance': ['empire', 'resistance'],
    'count': [empire_count, resistance_count]
})

print(counts_df)