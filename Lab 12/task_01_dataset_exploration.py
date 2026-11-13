"""TASK 1: Read and explore the supplied diabetes CSV dataset."""
import matplotlib
matplotlib.use("Agg")  # Save charts even when no GUI/display is available.
import matplotlib.pyplot as plt
from utils import load_dataset, OUTPUT_DIR, ensure_directories, TARGET, FEATURES


def run():
    ensure_directories()
    data = load_dataset()
    print("\n" + "=" * 57)
    print("TASK 01 - DATASET EXPLORATION")
    print("=" * 57)
    print(f"Total rows: {len(data)}")
    print(f"Total columns: {len(data.columns)}")
    print(f"Input features: {FEATURES}")
    print(f"Target column: {TARGET} (0 = No diabetes, 1 = Diabetes)")
    print("\nFirst five rows:")
    print(data.head().to_string(index=False))
    print("\nMissing cells in each column:")
    print(data.isnull().sum().to_string())
    print("\nClass distribution:")
    print(data[TARGET].value_counts().sort_index().to_string())

    # Some values of 0 in medical measurements can indicate unrecorded data.
    # They are kept unchanged for this introductory lab, not silently edited.
    possible_zero_missing = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    zero_counts = {name: int((data[name] == 0).sum()) for name in possible_zero_missing}
    print("\nZero counts in medical measurements (inspect before real-world use):")
    print(zero_counts)

    counts = data[TARGET].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    bars = ax.bar(["No diabetes (0)", "Diabetes (1)"], counts.values, color=["#2C7FB8", "#F18F3B"])
    for b in bars:
        ax.text(b.get_x() + b.get_width()/2, b.get_height()+6,
                str(int(b.get_height())), ha="center")
    ax.set(ylabel="Number of records", title="Diabetes dataset: Outcome distribution")
    ax.set_ylim(0, max(counts.values)*1.15)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "01_class_distribution.png", dpi=160)
    plt.close(fig)

    lines = [
        "TASK 01 - DATASET SUMMARY",
        f"Total rows: {len(data)}",
        f"Features: {', '.join(FEATURES)}",
        f"Target: {TARGET}",
        f"Class counts: {counts.to_dict()}",
        f"Missing cell count: {int(data.isna().sum().sum())}",
        f"Zero counts in measurements: {zero_counts}",
        "Note: zeros were not modified in this baseline lab.",
    ]
    (OUTPUT_DIR / "01_dataset_summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\nSaved output: outputs/01_dataset_summary.txt and 01_class_distribution.png")


if __name__ == "__main__":
    run()
