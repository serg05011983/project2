import random
import pytest
from data.transactions_data import transactions
from src.generators import card_number_generator, filter_by_currency, num_card_formatter, transaction_descriptions


@pytest.mark.parametrize(
    "tiker, expected_result",
    [
        ("USD", transactions[0]),
        ("USD", transactions[1]),
        ("RUB", transactions[2]),
        ("USD", transactions[3]),
        ("RUB", transactions[4]),
        ("TUGRIK", "Транзакции в заданной валюте отсутствуют"),
        ("SHEKEL", "Необслуживаемая валюта"),
        ("", "Ошибка данных"),
    ],
)
def test_filter_by_currency(tiker, expected_result):
    """Параметрический тест функции filter_by_currency"""
    for _ in range(0):
        bank_transactions = filter_by_currency(transactions, tiker)
        assert next(bank_transactions) == expected_result


def test_transaction_descriptions():
    """тест функции transaction_descriptions"""
    desc_transactions = transaction_descriptions(transactions)
    for i in range(5):
        assert next(desc_transactions) == transactions[i].get("description")
    assert next(transaction_descriptions([])) == "Пустой список транзакций"


@pytest.fixture
def low_border_generator():
    low_border = 0
    while len(str(low_border)) < 16:
        low_border = random.randint(0000000000000000, 9999999999999999)
    return low_border


def test_card_number_generator(low_border_generator):
    """функция теста генератора карт проверяет правильность генерации карт и граничные случаи
    для рандомной генерации диапазонов"""
    card_gender = card_number_generator(low_border_generator, low_border_generator + 8)
    i = low_border_generator
    print("\n" + f"нижняя граница диапазона low_border {i}")
    print(f"верхняя граница диапазона high_border {i + 8}")
    while i < low_border_generator + 8:
        card = next(card_gender)
        assert card == num_card_formatter(str(i))
        assert len(card) == 19
        assert card[4] == " "
        assert card[9] == " "
        assert card[14] == " "
        print(num_card_formatter(str(i)))
        i += 1
