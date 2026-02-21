import unittest

from src.processing import (count_categories, filter_by_currency,
                            filter_by_description, filter_by_status,
                            sort_by_date)


class TestProcessing(unittest.TestCase):

    def setUp(self):
        self.transactions = [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2019-12-08T22:46:21.314037",
                "operationAmount": {"amount": "40542", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Открытие вклада"
            },
            {
                "id": 2,
                "state": "CANCELED",
                "date": "2018-07-12T22:46:21.314037",
                "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту"
            },
            {
                "id": 3,
                "state": "executed",
                "date": "2020-01-01T10:00:00",
                "currency_code": "RUB",
                "amount": "500",
                "description": "Перевод организации"
            }
        ]

    def test_filter_by_description(self):
        result = filter_by_description(self.transactions, "открытие")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['id'], 1)

        result = filter_by_description(self.transactions, "ПЕРЕВ")
        self.assertEqual(len(result), 2)

    def test_count_categories(self):
        categories = ["Открытие вклада", "Перевод организации", "Unknown"]
        result = count_categories(self.transactions, categories)
        self.assertEqual(result["Открытие вклада"], 1)
        self.assertEqual(result["Перевод организации"], 1)
        self.assertEqual(result["Unknown"], 0)

    def test_filter_by_status(self):
        result = filter_by_status(self.transactions, "EXECUTED")
        self.assertEqual(len(result), 2)

        result = filter_by_status(self.transactions, "PENDING")
        self.assertEqual(len(result), 0)

    def test_sort_by_date(self):
        # Ascending
        result = sort_by_date(self.transactions, ascending=True)
        self.assertEqual(result[0]['id'], 2)  # 2018

        # Descending
        result = sort_by_date(self.transactions, ascending=False)
        self.assertEqual(result[0]['id'], 3)  # 2020

    def test_filter_by_currency(self):
        result = filter_by_currency(self.transactions, "RUB")
        self.assertEqual(len(result), 2)

        result = filter_by_currency(self.transactions, "USD")
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
