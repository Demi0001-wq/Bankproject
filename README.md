# Bank Project - Financial Transaction Processing

A Python application for processing financial transactions from various data formats (JSON, CSV, XLSX) with sensitive data masking.

## Features

- **Interactive CLI**: Comprehensive menu-driven interface to filter and view transactions.
- **Multi-format Support**: Read transactions from JSON, CSV (separated by `;`), and Excel files using `pandas`.
- **Sensitive Data Masking**: Securely mask card numbers (`XXXX XX** **** XXXX`) and account numbers (`**XXXX`).
- **Regex Search**: Search for specific words in transaction descriptions using regular expressions.
- **Transaction Analytics**: Count operations by category (e.g., Transfer, Opening) using `collections.Counter`.

## Installation

This project uses Poetry for dependency management.

1. Clone the repository and navigate to the project folder.
2. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

You can load and process transactions as follows:

```python
from src.utils import get_transactions
from src.masks import get_mask_card_number

# Load transactions from CSV
transactions = get_transactions("transactions.csv")

# Process and mask data
for tx in transactions:
    if 'from' in tx:
        masked_card = get_mask_card_number(tx['from'])
        print(f"Transaction from masked card: {masked_card}")
```

## Testing

Run tests using `pytest`:

```bash
set PYTHONPATH=.
pytest --cov=src
```
