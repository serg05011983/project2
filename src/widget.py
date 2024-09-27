from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_data_: str) -> str:
    """функция накладывает маску на номер карты или счёта пользователя"""
    if account_data_[0:4] == "Счёт":
        account_mask = get_mask_account(account_data_[5:])
    else:
        for i in range(len(account_data_)):
            if account_data_[i:].isdigit():
                account_mask = get_mask_card_number(account_data_[i:])
                return account_data_[0:i] + " " + account_mask
    return "Счёт " + account_mask


def get_date(date_: str) -> str:
    """Функция осуществляет переформатирование даты"""
    date_modify = '"' + date_[8:10] + "." + date_[5:7] + "." + date_[2:4] + '"'
    return date_modify


account_data = input("Введите аккаунт:  ")
date = input("Введите : дату в формате 2024-03-11T02:26:18.671407:  ")

print(mask_account_card(account_data))
print(get_date(date))
