import pandas as pd
import numpy as np

data = pd.read_csv('troop_movements.csv')

homeworlds, counts = np.unique(data['homeworld'], return_counts=True)
counts_df = pd.DataFrame({
    'homeworld': homeworlds,
    'count': counts
})

print(counts_df)
