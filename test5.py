import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('troop_movements.csv')

empire_or_resistance_count = data['empire_or_resistance'].value_counts().reset_index()
empire_or_resistance_count.columns = ['empire_or_resistance', 'count']

sns.set(style='whitegrid')

plt.figure(figsize=(10, 6))
ax = sns.barplot(x='empire_or_resistance', y='count', data=empire_or_resistance_count, palette=['blue', 'red'])

plt.title('Character Count by Empire or Resistance', fontsize=16)
plt.xlabel('Empire or Resistance', fontsize=14)
plt.ylabel('Count', fontsize=14)

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'bottom',
                fontsize=12)

plt.show()