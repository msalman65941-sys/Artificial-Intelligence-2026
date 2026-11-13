"""TASK 4: Evaluate model and save tree/metrics graphs and predictions."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import joblib
import pandas as pd
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay, classification_report
)
from sklearn.tree import plot_tree
from utils import get_train_test, OUTPUT_DIR, FEATURES, ensure_directories
from task_03_train_decision_tree import MODEL_FILE, train_model


def run():
    ensure_directories()
    if MODEL_FILE.exists():
        model = joblib.load(MODEL_FILE)
    else:
        model = train_model()[0]  # Also works if this task runs individually.
    _, X_test, _, y_test = get_train_test()
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    metrics = {
        "accuracy": float(accuracy_score(y_test, predictions)),
        "precision": float(precision_score(y_test, predictions, zero_division=0)),
        "recall": float(recall_score(y_test, predictions, zero_division=0)),
        "f1_score": float(f1_score(y_test, predictions, zero_division=0)),
    }
    print("\n" + "=" * 57)
    print("TASK 04 - MODEL EVALUATION AND VISUALIZATIONS")
    print("=" * 57)
    for metric, value in metrics.items():
        print(f"{metric.capitalize()}: {value:.4f}")
    print("\nClassification report:\n" + classification_report(
        y_test, predictions, labels=[0, 1], target_names=["No diabetes", "Diabetes"],
        zero_division=0
    ))
    pd.DataFrame([metrics]).to_csv(OUTPUT_DIR / "04_metrics.csv", index=False)
    result = X_test.copy()
    result["Actual_Outcome"] = y_test
    result["Predicted_Outcome"] = predictions
    result["Probability_Diabetes"] = probabilities
    result.to_csv(OUTPUT_DIR / "04_test_predictions.csv", index_label="OriginalRowIndex")

    fig, ax = plt.subplots(figsize=(6.4, 5.1))
    cm = confusion_matrix(y_test, predictions, labels=[0, 1])
    ConfusionMatrixDisplay(cm, display_labels=["No diabetes", "Diabetes"]).plot(
        ax=ax, cmap="Blues", values_format="d", colorbar=False
    )
    ax.set_title("Decision Tree - Confusion Matrix (Test Data)")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "04_confusion_matrix.png", dpi=160)
    plt.close(fig)

    importances = pd.Series(model.feature_importances_, index=FEATURES).sort_values()
    fig, ax = plt.subplots(figsize=(8, 4.7))
    importances.plot(kind="barh", ax=ax, color="#3F88C5")
    ax.set(xlabel="Feature importance", title="Decision Tree - Feature Importance")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "04_feature_importance.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(19, 10))
    plot_tree(
        model, feature_names=FEATURES, class_names=["No diabetes", "Diabetes"],
        filled=True, rounded=True, fontsize=8, ax=ax
    )
    ax.set_title("Week 12 - Decision Tree (Entropy, max_depth=4)", fontsize=17)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "04_decision_tree.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved outputs: metrics.csv, test_predictions.csv, confusion matrix, feature importance, tree plot")


if __name__ == "__main__":
    run()
