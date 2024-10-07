import pytest
from src.masks import get_mask_account, get_mask_card_number
from typing import Any


# тесты с параметризацией
@pytest.mark.parametrize(
    "card_num_, expected_result",
    [("1122334455667788", "1122 33** **** 7788"), ("11223344556677889", "Ошибка ввода"), ("", "Ошибка ввода")],
)
def test_get_mask_card_number(card_num_: str, expected_result: str) -> Any:
    """тест функции маскировки карты"""
    assert get_mask_card_number(card_num_) == expected_result


@pytest.mark.parametrize(
    "account, expected_result",
    [("11122233344455566677", "**6677"), ("111222333444555666777", "Ошибка ввода"), ("", "Ошибка ввода")],
)
def test_get_mask_account(account: str, expected_result: str) -> Any:
    """тест функции маскировки номера счёта"""
    assert get_mask_account(account) == expected_result
