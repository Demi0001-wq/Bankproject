import re
from collections import Counter
from typing import Dict, List


def filter_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Filters transactions whose description contains the search string using regular expressions.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [tx for tx in transactions if tx.get('description') and pattern.search(tx['description'])]


def count_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Counts occurrences of specified categories in transaction descriptions.
    """
    descriptions = [tx.get('description', '') for tx in transactions]
    counts = Counter(descriptions)
    return {cat: counts[cat] for cat in categories}


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """
    Filters transactions by their state (case-insensitive).
    """
    status = status.upper()
    return [tx for tx in transactions if str(tx.get('state')).upper() == status]


def sort_by_date(transactions: List[Dict], ascending: bool = True) -> List[Dict]:
    """
    Sorts transactions by date.
    """
    return sorted(
        transactions,
        key=lambda x: str(x.get('date', '')),
        reverse=not ascending
    )


def filter_by_currency(transactions: List[Dict], currency: str = 'RUB') -> List[Dict]:
    """
    Filters transactions for a specific currency.
    """
    return [
        tx for tx in transactions
        if (tx.get('operationAmount') and tx['operationAmount'].get('currency', {}).get('code') == currency) or
           (tx.get('currency_code') == currency)
    ]
