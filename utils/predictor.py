def predict_burnout(study, sleep, stress, assignment, attendance):

    try:
        # Burnout Score Formula
        score = (
            study * 4 +
            stress * 6 +
            assignment * 4 -
            sleep * 2 -
            attendance * 0.3
        )

        score = max(0, score)

        # Burnout Level Conditions
        if score < 33:
            level = "Low"
        elif score < 66:
            level = "Medium"
        else:
            level = "High"

        return score, level

    except Exception as e:
        print("Prediction Error:", e)
        return 0, "Low"