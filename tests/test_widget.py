import unittest
from src.widget import mask_account_card, get_date

class TestWidget(unittest.TestCase):
    def test_mask_account_card_visa(self):
        self.assertEqual(mask_account_card("Visa Platinum 7000792289606635"), "Visa Platinum 7000 79** **** 6635")

    def test_mask_account_card_account(self):
        self.assertEqual(mask_account_card("Счет 73654108430135874305"), "Счет **4305")

    def test_mask_account_card_empty(self):
        self.assertEqual(mask_account_card(""), "")

    def test_get_date_standard(self):
        self.assertEqual(get_date("2024-03-11T02:26:18.671407"), "11.03.2024")

    def test_get_date_empty(self):
        self.assertEqual(get_date(""), "")
