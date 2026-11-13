"""TASK 3: Train the Decision Tree model (uses entropy for splitting)."""
import joblib
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score
from utils import get_train_test, MODEL_DIR, OUTPUT_DIR, FEATURES, RANDOM_STATE, ensure_directories

MODEL_FILE = MODEL_DIR / "decision_tree_model.joblib"


def train_model():
    X_train, X_test, y_train, y_test = get_train_test()
    # A small tree is easier to interpret and reduces overfitting (pruning).
    model = DecisionTreeClassifier(
        criterion="entropy", max_depth=4, min_samples_leaf=10,
        random_state=RANDOM_STATE,
    )
    model.fit(X_train, y_train)
    return model, X_train, X_test, y_train, y_test


def run():
    ensure_directories()
    model, X_train, X_test, y_train, y_test = train_model()
    joblib.dump(model, MODEL_FILE)
    train_accuracy = accuracy_score(y_train, model.predict(X_train))
    test_accuracy = accuracy_score(y_test, model.predict(X_test))
    print("\n" + "=" * 57)
    print("TASK 03 - TRAIN DECISION TREE")
    print("=" * 57)
    print(f"Training records: {len(X_train)}; Test records: {len(X_test)}")
    print("Model: DecisionTreeClassifier(criterion='entropy', max_depth=4, min_samples_leaf=10)")
    print(f"Training accuracy: {train_accuracy:.4f}")
    print(f"Testing accuracy:  {test_accuracy:.4f}")
    print(f"Depth: {model.get_depth()}; Leaves: {model.get_n_leaves()}")
    print(f"Model saved: {MODEL_FILE.relative_to(MODEL_DIR.parent)}")
    rules = export_text(model, feature_names=FEATURES)
    (OUTPUT_DIR / "03_decision_tree_rules.txt").write_text(rules, encoding="utf-8")
    print("Decision rules saved: outputs/03_decision_tree_rules.txt")


if __name__ == "__main__":
    run()
