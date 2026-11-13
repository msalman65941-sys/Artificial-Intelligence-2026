"""TASK 2: Calculate entropy & information gain, matching slides 9-13."""
import math
from collections import Counter
from sklearn.tree import DecisionTreeClassifier
from utils import get_train_test, FEATURES, OUTPUT_DIR, ensure_directories, RANDOM_STATE


def entropy(values):
    """H(S) = -sum(p_i * log2(p_i))."""
    counts = Counter(values)
    total = sum(counts.values())
    if total == 0:
        return 0.0
    return -sum((count/total) * math.log2(count/total)
                for count in counts.values() if count > 0)


def information_gain(labels, left_labels, right_labels):
    """IG = H(parent) - [n_left/n * H(left) + n_right/n * H(right)]."""
    total = len(labels)
    parent_h = entropy(labels)
    left_h = entropy(left_labels)
    right_h = entropy(right_labels)
    weighted_h = (len(left_labels)/total)*left_h + (len(right_labels)/total)*right_h
    return parent_h, left_h, right_h, weighted_h, parent_h-weighted_h


def run():
    ensure_directories()
    X_train, X_test, y_train, y_test = get_train_test()
    print("\n" + "=" * 57)
    print("TASK 02 - ENTROPY AND INFORMATION GAIN")
    print("=" * 57)
    example_h = entropy([1]*9 + [0]*5)  # 9/14 and 5/14 from the lecture slide
    print(f"Lecture slide example: 9 positive, 5 negative -> Entropy = {example_h:.4f}")
    print(f"Actual training Outcome entropy: {entropy(y_train):.4f}")

    # Find the best first split, using entropy (the lesson's splitting concept).
    # scikit-learn builds binary CART-style trees, not literal categorical ID3.
    stump = DecisionTreeClassifier(criterion="entropy", max_depth=1, random_state=RANDOM_STATE)
    stump.fit(X_train, y_train)
    tree = stump.tree_
    feature_name = FEATURES[tree.feature[0]]
    threshold = float(tree.threshold[0])
    mask = X_train[feature_name] <= threshold
    left_labels = y_train[mask]
    right_labels = y_train[~mask]
    parent_h, left_h, right_h, weighted_h, gain = information_gain(
        y_train, left_labels, right_labels
    )
    lines = [
        "TASK 02 - ENTROPY AND INFORMATION GAIN",
        f"Slide 9-10 example (9/14 vs 5/14) entropy: {example_h:.6f}",
        f"Training records: {len(y_train)}",
        f"Parent entropy: {parent_h:.6f}",
        f"Best first split (trained on TRAINING data only): {feature_name} <= {threshold:.3f}",
        f"Left records (<=): {len(left_labels)}, left entropy: {left_h:.6f}",
        f"Right records (>): {len(right_labels)}, right entropy: {right_h:.6f}",
        f"Weighted child entropy: {weighted_h:.6f}",
        f"Information gain = parent - weighted = {gain:.6f}",
        "NOTE: sklearn uses CART-style binary splits, with entropy criterion; not exact classic ID3.",
    ]
    print("\n".join(lines))
    (OUTPUT_DIR / "02_entropy_information_gain.txt").write_text("\n".join(lines)+"\n", encoding="utf-8")
    print("Saved output: outputs/02_entropy_information_gain.txt")


if __name__ == "__main__":
    run()
