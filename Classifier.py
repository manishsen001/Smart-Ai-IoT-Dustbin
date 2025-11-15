import pickle

model_path = "ml/model.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

def classify(trash_features):
    prediction = model.predict([trash_features])
    return prediction[0]