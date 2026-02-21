import io
import unittest
from unittest.mock import patch

from main import main


class TestMain(unittest.TestCase):

    @patch('main.get_transactions')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_workflow_json(self, mock_stdout, mock_input, mock_get_transactions):
        # Mocking user inputs
        # 1: JSON choice
        # EXECUTED: Status choice
        # Нет: Sort choice
        # Нет: Currency choice
        # Нет: Search choice
        mock_input.side_effect = ['1', 'EXECUTED', 'нет', 'нет', 'нет']

        # Mocking transactions
        mock_get_transactions.return_value = [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2019-12-08T22:46:21",
                "operationAmount": {"amount": "40542", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Открытие вклада",
                "to": "Счет 12345678123456781234"
            }
        ]

        main()

        output = mock_stdout.getvalue()
        self.assertIn("Для обработки выбран JSON-файл", output)
        self.assertIn("Операции отфильтрованы по статусу \"EXECUTED\"", output)
        self.assertIn("Всего банковских операций в выборке: 1", output)
        self.assertIn("08.12.2019 Открытие вклада", output)
        self.assertIn("Счет **1234", output)

    @patch('main.get_transactions')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_main_no_transactions(self, mock_stdout, mock_input, mock_get_transactions):
        mock_input.side_effect = ['1', 'EXECUTED', 'нет', 'нет', 'нет']
        mock_get_transactions.return_value = []

        main()
        output = mock_stdout.getvalue()
        self.assertIn("Не удалось загрузить данные", output)


if __name__ == "__main__":
    unittest.main()
