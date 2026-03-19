def predict_burnout(study, sleep, stress, assignment, attendance):

    try:
        # Rule-based burnout prediction (NO formula)

        # High burnout condition
        if stress >= 8 or sleep <= 4 or assignment >= 8:
            level = "High"
            score = 80

        # Medium burnout condition
        elif stress >= 5 or sleep <= 6 or assignment >= 5:
            level = "Medium"
            score = 50

        # Low burnout condition
        else:
            level = "Low"
            score = 20

        return score, level

    except Exception as e:
        print("Prediction Error:", e)
        return 0, "Low"