import json
import os
from typing import Dict, List

import pandas as pd


def load_transactions_from_json(file_path: str) -> List[Dict]:
    """
    Loads transactions from a JSON file.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def load_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Loads transactions from a CSV file using pandas.
    """
    if not os.path.exists(file_path):
        return []

    try:
        df = pd.read_csv(file_path, sep=';')
        return df.to_dict(orient='records')
    except Exception:
        return []


def load_transactions_from_xlsx(file_path: str) -> List[Dict]:
    """
    Loads transactions from an Excel file using pandas.
    """
    if not os.path.exists(file_path):
        return []

    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')
    except Exception:
        return []


def get_transactions(file_path: str) -> List[Dict]:
    """
    General function to load transactions based on file extension.
    """
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == '.json':
        return load_transactions_from_json(file_path)
    elif ext == '.csv':
        return load_transactions_from_csv(file_path)
    elif ext in ['.xlsx', '.xls']:
        return load_transactions_from_xlsx(file_path)
    else:
        return []
