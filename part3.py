import pandas as pd
import pickle


df = pd.read_csv("troop_movements_1m.csv")


df['unit_type'] = df['unit_type'].replace("invalid_unit", "unknown")
df[['location_x', 'location_y']] = df[['location_x', 'location_y']].ffill()



df.to_parquet("troop_movements_1m.parquet", engine="pyarrow")


with open("trained_model.pkl", "rb") as f:
    model, feature_names = pickle.load(f)


X_1m = pd.get_dummies(df[['homeworld', 'unit_type']])
X_1m = X_1m.reindex(columns=feature_names, fill_value=0)


df['is_resistance_pred'] = model.predict(X_1m)

print(df[['timestamp', 'unit_id', 'unit_type', 'location_x', 'location_y', 'destination_x', 'destination_y', 'homeworld', 'is_resistance_pred']].head(10))

df.to_csv("troop_movements_1m_with_predictions.csv")
