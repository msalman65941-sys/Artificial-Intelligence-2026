"""Helpers shared by all Week 12 Decision Tree tasks."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "diabetes.csv"
OUTPUT_DIR = ROOT / "outputs"
MODEL_DIR = ROOT / "model"
TARGET = "Outcome"
FEATURES = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]
RANDOM_STATE = 42
TEST_SIZE = 0.20

def load_dataset():
    """Load the exact dataset supplied with the lab; do not alter its rows."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")
    data = pd.read_csv(DATA_PATH)
    expected = FEATURES + [TARGET]
    missing = [column for column in expected if column not in data.columns]
    if missing:
        raise ValueError(f"Missing required dataset columns: {missing}")
    if data[expected].isna().any().any():
        raise ValueError("CSV contains missing cells; handle them before training.")
    if not set(data[TARGET].unique()).issubset({0, 1}):
        raise ValueError("Outcome must contain only 0 or 1.")
    return data

def get_train_test():
    """Always use the same stratified train/test split across tasks."""
    data = load_dataset()
    X = data[FEATURES]
    y = data[TARGET]
    return train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )

def ensure_directories():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
