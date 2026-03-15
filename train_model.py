import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset
data = {
    "study_hours": [2,4,6,8,3,5,7],
    "sleep_hours": [8,7,6,5,7,6,4],
    "stress_level": [3,5,7,9,4,6,8],
    "burnout": [0,0,1,1,0,1,1]
}

df = pd.DataFrame(data)

X = df[["study_hours","sleep_hours","stress_level"]]
y = df["burnout"]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("burnout_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")