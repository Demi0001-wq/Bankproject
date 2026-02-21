def get_mask_card_number(card_number: str) -> str:
    """
    Masks a card number in the format XXXX XX** **** XXXX.
    """
    if not card_number:
        return ""

    # Remove any whitespaces
    card_number = card_number.replace(" ", "")

    # Masking logic
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Masks an account number in the format **XXXX (last 4 digits).
    """
    if not account_number:
        return ""

    return f"**{account_number[-4:]}"
