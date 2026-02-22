import unittest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

class TestGenerators(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Desc 1"},
            {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Desc 2"},
            {"id": 3, "currency_code": "USD", "description": "Desc 3"}
        ]

    def test_filter_by_currency(self):
        usd_txs = list(filter_by_currency(self.transactions, "USD"))
        self.assertEqual(len(usd_txs), 2)
        self.assertEqual(usd_txs[0]["id"], 1)
        self.assertEqual(usd_txs[1]["id"], 3)

    def test_transaction_descriptions(self):
        descriptions = list(transaction_descriptions(self.transactions))
        self.assertEqual(descriptions, ["Desc 1", "Desc 2", "Desc 3"])

    def test_card_number_generator(self):
        gen = card_number_generator(1, 2)
        self.assertEqual(next(gen), "0000 0000 0000 0001")
        self.assertEqual(next(gen), "0000 0000 0000 0002")
