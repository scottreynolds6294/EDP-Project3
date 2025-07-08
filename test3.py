import pandas as pd
import numpy as np

data = pd.read_csv('troop_movements.csv')

unit_type_groups = data.groupby('unit_type')
unit_counts = unit_type_groups.size()

counts_df = pd.DataFrame({
    'unit_type': unit_counts.index,
    'count': unit_counts.values
})

print(counts_df)