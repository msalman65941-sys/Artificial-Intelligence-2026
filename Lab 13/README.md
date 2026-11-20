# Lab 13 — Decision Trees in Python
**Student:** Muhammad Salman 
**SAP ID:** 72373  
**Section:** AI 3-1

## Folder structure
- `Muhammad Salman_72373_DecisionTree_Lab.ipynb` — complete Jupyter notebook (Markdown + code + evaluation).
- `data/` — place the three required Kaggle CSV files here.
- `outputs/` — reserved for exported results/figures if you choose to save them.
- `model/` — reserved for saved trained models.
- `requirements.txt` — Python packages required.
- `download_datasets.py` — helper that downloads the three datasets using Kaggle API credentials.

## Required datasets
1. Heart Failure Prediction: `heart.csv` — target `HeartDisease`
   https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction
2. Telco Customer Churn: `Telco-Customer-Churn.csv` — target `Churn`
   https://www.kaggle.com/datasets/blastchar/telco-customer-churn
3. Mushroom Classification: `mushrooms.csv` — target `class`
   https://www.kaggle.com/datasets/uciml/mushroom-classification

**Important:** Do not use the Diabetes dataset. The lab manual specifically requires the three datasets listed above.

## Setup
1. Install Python 3.10+ and Jupyter (or use VS Code with the Jupyter extension).
2. Open a terminal in this folder and run:
   `pip install -r requirements.txt`
3. Download the datasets using the Kaggle API (instructions below), or download each CSV manually from its Kaggle page and put it inside `data/`.
4. Open `Shan_72387_DecisionTree_Lab.ipynb`.
5. Run all cells from top to bottom.

## Kaggle API download (optional)
- Sign in to Kaggle → Account → Create New Token.
- Save the downloaded `kaggle.json` in the standard Kaggle location:
  - Windows: `%USERPROFILE%\.kaggle\kaggle.json`
  - Linux/macOS: `~/.kaggle/kaggle.json`
- Then run:
  `python download_datasets.py`

The notebook checks both the current folder and `data/` for the CSV files.
