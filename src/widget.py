from .masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Masks a string containing either a card or an account number.
    Identifies the type based on descriptive words (e.g., 'Счет', 'Visa').
    """
    if not info or (isinstance(info, float) and str(info) == 'nan'):
        return ""

    info = str(info)
    parts = info.split()
    label = " ".join(parts[:-1])
    number = parts[-1]

    if "Счет" in label or "Account" in label:
        return f"{label} {get_mask_account(number)}"
    else:
        return f"{label} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Converts a date string from 'YYYY-MM-DDTHH:MM:SS.mmmmmm' format to 'DD.MM.YYYY'.
    """
    if not date_str:
        return ""

    # Assuming YYYY-MM-DD format within the string
    date_part = date_str.split('T')[0]
    date_split = date_part.split('-')

    if len(date_split) == 3:
        return f"{date_split[2]}.{date_split[1]}.{date_split[0]}"

    return date_str
