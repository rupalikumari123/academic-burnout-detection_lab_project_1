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

        # Classification
        if score < 33:
            level = 0   # Low
        elif score < 66:
            level = 1   # Medium
        else:
            level = 2   # High

        return level, score

    except Exception as e:
        print("Prediction Error:", e)
        return 0, 0