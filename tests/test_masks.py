import pytest
from src.masks import get_mask_account, get_mask_card_number

#обычные тесты
#def test_get_mask_card_number():
#    assert get_mask_card_number("1122334455667788") == "1122 33** **** 7788"

#def test_get_mask_account():
#    assert get_mask_account('11122233344455566677') == '**6677'

#тесты с фикстурой
@pytest.fixture
def card():
    return "1122334455667788"

@pytest.fixture
def account():
    return '11122233344455566677'
def test_get_mask_card_number(card):
    assert get_mask_card_number(card) == "1122 33** **** 7788"

def test_get_mask_account(account):
    assert get_mask_account(account) == '**6677'

#тесты с параметризацией
