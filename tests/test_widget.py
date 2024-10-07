import pytest
from src.widget import get_date, mask_account_card
from typing import Any


@pytest.mark.parametrize(
    "account_card, expected_result",
    [
        ("Visa 3300303024671199", "Visa 3300 30** **** 1199"),
        ("1122334455667788", "1122 33** **** 7788"),
        ("Visa 33003030246771199", "Ошибка ввода"),
        ("Счёт 11122233344455566677", "Счёт **6677"),
        ("Счёт 111222333444555666770", "Ошибка ввода"),
        ("", "Ошибка ввода"),
    ],
)
def test_mask_account_card(account_card: str, expected_result: str) -> Any:
    """тест функции маскировки карты или номера счёта"""
    assert mask_account_card(account_card) == expected_result


@pytest.mark.parametrize(
    "gen_date, expected_result",
    [
        ("2024-03-11T02:26:18.671407", '"11.03.24"'),
        ("2024-03-11T02:207", '"11.03.24"'),
        ("2024+03-11T02:26:18.671407", "Ошибка ввода"),
        ("2024-03+11T02:26:18.671407", "Ошибка ввода"),
        ("202W-03-11T02:26:18.671407", "Ошибка ввода"),
        ("20F4-03-11T02:26:18.671407", "Ошибка ввода"),
        ("2P24-03-11T02:26:18.671407", "Ошибка ввода"),
        ("A024-03-11T02:26:18.671407", "Ошибка ввода"),
        ("2024-Z3-11T02:26:18.671407", "Ошибка ввода"),
        ("2024-3Z-11T02:26:18.671407", "Ошибка ввода"),
        ("2024-03-B1T02:26:18.671407", "Ошибка ввода"),
        ("2024-03-1TT02:26:18.671407", "Ошибка ввода"),
        ("2024-03-11", '"11.03.24"'),
        ("2024-03-1ZT02:26:18.671407", "Ошибка ввода"),
        ("", "Ошибка ввода"),
    ],
)
def test_get_date(gen_date: str, expected_result: str) -> Any:
    """тест функции маскировки карты или номера счёта"""
    assert get_date(gen_date) == expected_result
