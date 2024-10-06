import pytest
from src.widget import get_date, mask_account_card

@pytest.fixture
def gen_date():
    return '2024-03-11T02:26:18.671407'

@pytest.fixture
def account_card():
    return '1122334455667788'

def test_mask_account_card(account_card):
    assert mask_account_card(account_card) == '"1122 33** **** 7788"'

def test_get_date(gen_date):
    assert get_date(gen_date) == '"11.03.24"'