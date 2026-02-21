from src.masks import get_mask_account, get_mask_card_number
from src.utils import get_transactions


def main():
    """
    Main entry point for the banking project.
    """
    # Paths to the provided files
    files = [
        "transactions.csv",
        "transactions_excel.xlsx"
    ]

    for file_name in files:
        print(f"\n{'='*20}")
        print(f"Loading from: {file_name}")
        print(f"{'='*20}")

        transactions = get_transactions(file_name)

        if not transactions:
            print(f"No transactions found or error loading {file_name}")
            continue

        print(f"Total transactions: {len(transactions)}")

        # Show first 3 for verification
        for i, tx in enumerate(transactions[:3]):
            print(f"\nTransaction {i+1}:")
            print(f"  ID: {tx.get('id')}")
            print(f"  State: {tx.get('state')}")
            print(f"  Amount: {tx.get('amount')} {tx.get('currency_name') or tx.get('currency_code')}")

            # Example of using masking if description contains card or account info
            desc = tx.get('description', '')
            print(f"  Description: {desc}")

            # Simulated masking output (since we don't know the exact columns for numbers yet)
            # In a real scenario, we'd extract and mask.
            # Here we just show the functions work.
            print(f"  Mock Masked Card: {get_mask_card_number('1234567812345678')}")
            print(f"  Mock Masked Account: {get_mask_account('73654108430135874305')}")


if __name__ == "__main__":
    main()
