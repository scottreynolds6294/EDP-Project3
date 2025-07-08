import pickle
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

with open('trained_model.pkl', 'rb') as file:
    contents = pickle.load(file)
    model = contents[0]
    feature_names = contents[1] 

print(type(model))


@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    if isinstance(data, dict):
        data = [data]

    input_df = pd.DataFrame(data)
    input_df = input_df.reindex(columns=feature_names, fill_value=0)

    prediction = model.predict(input_df)

    return jsonify(prediction.tolist())

if __name__ == '__main__':
    app.run(port=5000)
