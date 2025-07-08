import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

df = pd.read_csv("troop_movements.csv")

df['is_resistance'] = df['empire_or_resistance'] == 'resistance'

# Encode features
X = pd.get_dummies(df[['homeworld', 'unit_type']])
y = df['is_resistance']

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

with open("trained_model.pkl", "wb") as f:
    pickle.dump((model, list(X.columns)), f)

print("Model and feature names saved to trained_model.pkl.")
