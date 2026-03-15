# import pickle
# import numpy as np

# # Load trained model
# model = pickle.load(open("burnout_model.pkl", "rb"))

# def predict_burnout(study_hours, sleep_hours, stress_level):

#     # Model expects 3 features
#     data = np.array([[study_hours, sleep_hours, stress_level]])

#     prediction = model.predict(data)

#     return prediction[0]




import pickle
import numpy as np

# Load Model
model = pickle.load(open("burnout_model.pkl", "rb"))

def predict_burnout(study, sleep, stress):

    try:
        features = np.array([[study, sleep, stress]])
        prediction = model.predict(features)
        return prediction[0]

    except Exception as e:
        print("Prediction Error:", e)
        return 0