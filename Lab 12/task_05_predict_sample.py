"""TASK 5: Make one prediction with the trained Decision Tree."""
import joblib
import pandas as pd
from utils import get_train_test, OUTPUT_DIR, FEATURES, ensure_directories
from task_03_train_decision_tree import MODEL_FILE, train_model


def run():
    ensure_directories()
    if MODEL_FILE.exists():
        model = joblib.load(MODEL_FILE)
    else:
        model = train_model()[0]

    _, X_test, _, y_test = get_train_test()
    # Default: take a real held-out row from the uploaded dataset.
    # For your own example, replace the dictionary below with your 8 values.
    sample = X_test.iloc[[0]].copy()
    true_label = int(y_test.iloc[0])

    # Example of manual input (uncomment to use your own values):
    # sample = pd.DataFrame([{
    #     "Pregnancies": 2, "Glucose": 130, "BloodPressure": 72,
    #     "SkinThickness": 25, "Insulin": 90, "BMI": 31.0,
    #     "DiabetesPedigreeFunction": 0.5, "Age": 35,
    # }], columns=FEATURES)
    # true_label = None

    prediction = int(model.predict(sample)[0])
    probability = float(model.predict_proba(sample)[0, 1])
    label = "Diabetes (1)" if prediction == 1 else "No diabetes (0)"
    lines = [
        "TASK 05 - SAMPLE PREDICTION",
        "Input row:", sample.to_string(index=False),
        f"Predicted class: {label}",
        f"Model probability for class 1: {probability:.3f}",
        f"Actual class (if using test row): {true_label}",
        "Educational example only. Not a medical diagnosis or calibrated clinical risk estimate.",
    ]
    print("\n" + "=" * 57)
    print("\n".join(lines))
    (OUTPUT_DIR / "05_sample_prediction.txt").write_text("\n".join(lines)+"\n", encoding="utf-8")


if __name__ == "__main__":
    run()
