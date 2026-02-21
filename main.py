import os

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_currency, filter_by_description, filter_by_status, sort_by_date
from src.utils import get_transactions


def main():
    """
    Main entry point for interactive banking transaction processing.
    """
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("\nПользователь: ").strip()
        if choice == '1':
            file_path = os.path.join("data", "operations.json")
            print("Программа: Для обработки выбран JSON-файл.")
            break
        elif choice == '2':
            file_path = os.path.join("data", "transactions.csv")
            print("Программа: Для обработки выбран CSV-файл.")
            break
        elif choice == '3':
            file_path = os.path.join("data", "transactions_excel.xlsx")
            print("Программа: Для обработки выбран XLSX-файл.")
            break
        else:
            print("Программа: Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")

    transactions = get_transactions(file_path)
    if not transactions:
        print(f"Программа: Не удалось загрузить данные из {file_path}")
        return

    # Status filtering
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(available_statuses)}")
        status_input = input("Пользователь: ").strip().upper()

        if status_input in available_statuses:
            transactions = filter_by_status(transactions, status_input)
            print(f"Программа: Операции отфильтрованы по статусу \"{status_input}\"")
            break
        else:
            print(f"Программа: Статус операции \"{status_input}\" недоступен.")

    # Sorting by date
    sort_choice = input(
        "\nПрограмма: Отсортировать операции по дате? Да/Нет\nПользователь: "
    ).strip().lower()
    if sort_choice == 'да':
        order_choice = input(
            "Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: "
        ).strip().lower()
        ascending = True if 'возраст' in order_choice else False
        transactions = sort_by_date(transactions, ascending=ascending)

    # Filter by currency
    currency_choice = input(
        "\nПрограмма: Выводить только рублевые транзакции? Да/Нет\nПользователь: "
    ).strip().lower()
    if currency_choice == 'да':
        transactions = filter_by_currency(transactions, "RUB")

    # Filter by search string
    search_choice = input(
        "\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: "
    ).strip().lower()
    if search_choice == 'да':
        search_word = input("Программа: Введите слово для поиска\nПользователь: ").strip()
        transactions = filter_by_description(transactions, search_word)

    print("\nПрограмма: Распечатываю итоговый список транзакций...")

    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Программа: Всего банковских операций в выборке: {len(transactions)}")

    for tx in transactions:
        # Date formatting (assuming YYYY-MM-DDTHH:MM:SS)
        date_str = tx.get('date', 'Unknown Date')
        if 'T' in date_str:
            date_part = date_str.split('T')[0]
            display_date = ".".join(reversed(date_part.split('-')))
        else:
            display_date = date_str

        desc = tx.get('description', 'No Description')

        # Amount formatting
        amount = tx.get('amount')
        currency = tx.get('currency_name') or tx.get('currency_code')
        if not amount and tx.get('operationAmount'):
            amount = tx['operationAmount'].get('amount')
            currency = tx['operationAmount'].get('currency', {}).get('name')

        # From/To masking
        from_info = tx.get('from', '')
        to_info = tx.get('to', '')

        def mask_label(info):
            if not info:
                return ""
            parts = info.split()
            label = " ".join(parts[:-1])
            number = parts[-1]
            if "Счет" in label or "Account" in label:
                return f"{label} {get_mask_account(number)}"
            else:
                return f"{label} {get_mask_card_number(number)}"

        print(f"\n{display_date} {desc}")
        if from_info:
            print(f"{mask_label(from_info)} -> {mask_label(to_info)}")
        else:
            print(f"{mask_label(to_info)}")
        print(f"Сумма: {amount} {currency}")


if __name__ == "__main__":
    main()
