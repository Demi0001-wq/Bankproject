from typing import List, Dict, Generator

def filter_by_currency(transactions: List[Dict], currency: str) -> Generator[Dict, None, None]:
    """
    Generator that yields transactions filtered by a specific currency.
    """
    for tx in transactions:
        amount_data = tx.get('operationAmount', {})
        currency_data = amount_data.get('currency', {})
        if currency_data.get('code') == currency:
            yield tx
        elif tx.get('currency_code') == currency:
            yield tx

def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Generator that yields descriptions of transactions one by one.
    """
    for tx in transactions:
        yield tx.get('description', 'No Description')

def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Generator that yields card numbers in format XXXX XXXX XXXX XXXX.
    """
    for i in range(start, end + 1):
        num_str = str(i).zfill(16)
        formatted = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted
