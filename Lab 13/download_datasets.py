"""Download the three Lab 13 datasets using the Kaggle API.

Prerequisite: configure Kaggle API credentials (kaggle.json).
Run from this folder: python download_datasets.py
"""
from pathlib import Path
import subprocess
import sys
import zipfile

DATA = Path("data")
DATA.mkdir(exist_ok=True)

DATASETS = [
    ("fedesoriano/heart-failure-prediction", "heart"),
    ("blastchar/telco-customer-churn", "telco"),
    ("uciml/mushroom-classification", "mushroom"),
]

for slug, label in DATASETS:
    print(f"\nDownloading {label}: {slug}")
    result = subprocess.run(
        [sys.executable, "-m", "kaggle", "datasets", "download",
         "-d", slug, "-p", str(DATA), "--force"],
        check=False
    )
    if result.returncode != 0:
        raise SystemExit(
            "Kaggle download failed. Check that kaggle.json is configured "
            "and that you have accepted the dataset rules if required."
        )

    # Extract only the archive(s) downloaded for this dataset.
    for archive in DATA.glob("*.zip"):
        try:
            with zipfile.ZipFile(archive) as zf:
                zf.extractall(DATA)
            archive.unlink()
        except zipfile.BadZipFile:
            print(f"Skipping invalid archive: {archive}")

print("\nDownloads extracted under data/.")
print("If filenames are nested in subfolders, move the required CSVs directly into data/:")
print("  heart.csv, Telco-Customer-Churn.csv, mushrooms.csv")
