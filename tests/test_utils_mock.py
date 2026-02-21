import unittest
from unittest.mock import patch

import pandas as pd

from src.utils import (get_transactions, load_transactions_from_csv,
                       load_transactions_from_xlsx)


class TestTransactionLoading(unittest.TestCase):

    @patch('pandas.read_csv')
    @patch('os.path.exists')
    def test_load_transactions_from_csv_mock(self, mock_exists, mock_read_csv):
        # Mock file data
        mock_exists.return_value = True
        mock_df = pd.DataFrame([{
            "id": 1,
            "state": "EXECUTED",
            "amount": 100
        }])
        mock_read_csv.return_value = mock_df

        result = load_transactions_from_csv("dummy.csv")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 1)
        mock_read_csv.assert_called_once_with("dummy.csv", sep=';')

    @patch('pandas.read_excel')
    @patch('os.path.exists')
    def test_load_transactions_from_xlsx_mock(self, mock_exists, mock_read_excel):
        mock_exists.return_value = True
        mock_df = pd.DataFrame([{
            "id": 2,
            "state": "PENDING",
            "amount": 200
        }])
        mock_read_excel.return_value = mock_df

        result = load_transactions_from_xlsx("dummy.xlsx")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 2)
        mock_read_excel.assert_called_once_with("dummy.xlsx")

    def test_get_transactions_invalid_extension(self):
        result = get_transactions("test.txt")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
