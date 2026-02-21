import os
import unittest

from src.masks import get_mask_account, get_mask_card_number
from src.utils import get_transactions


class TestFinancialApp(unittest.TestCase):

    def test_mask_card_number(self):
        self.assertEqual(get_mask_card_number("1234567812345678"), "1234 56** **** 5678")
        self.assertEqual(get_mask_card_number(""), "")

    def test_mask_account(self):
        self.assertEqual(get_mask_account("73654108430135874305"), "**4305")
        self.assertEqual(get_mask_account(""), "")

    def test_csv_loading(self):
        # Create a temp csv for testing if needed, or use the project one
        file_path = "transactions.csv"
        if os.path.exists(file_path):
            records = get_transactions(file_path)
            self.assertIsInstance(records, list)
            if records:
                self.assertIn('id', records[0])

    def test_xlsx_loading(self):
        file_path = "transactions_excel.xlsx"
        if os.path.exists(file_path):
            records = get_transactions(file_path)
            self.assertIsInstance(records, list)
            if records:
                self.assertIn('id', records[0])


if __name__ == "__main__":
    unittest.main()
