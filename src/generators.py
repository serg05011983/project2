# from decorators import log
# from typing import Any
import random

# from data.transactions_data import transactions


def filter_by_currency(transactions_, tiker):
    "функция выдаёт из принимаемого словаря транзакции в заданной валюте"
    enable_tiker = ["RUB", "USD", "EURO", "CNY", "BTC", "TUGRIK"]
    if len(transactions_) > 0:
        operationAmount = []
        for transaction in transactions_:
            for keys, values in transaction.items():
                if keys == "operationAmount":
                    operationAmount = values
                    for keys_, values_ in operationAmount.items():
                        if keys_ == "currency":
                            if values_.get("code") in enable_tiker:
                                if values_.get("code") == tiker:
                                    yield transaction
                            else:
                                yield "Необслуживаемая валюта"
        yield "Транзакции в заданной валюте отсутствуют"
    else:
        yield "Пустой словарь"


def transaction_descriptions(transactions_):
    """функция возвращает наименование банковских операций из принимаемого словаря"""
    if len(transactions_) > 0:
        for transaction in transactions_:
            for keys, values in transaction.items():
                if keys == "description":
                    yield values
    else:
        yield "Пустой список транзакций"


def clone(num: int) -> str:
    """функция клонирования нуля добавляет недостающее число в номер карты"""
    return "0" * num


def num_card_formatter(s: str) -> str:
    """функция преобразует 16-ричную строку к формату карты"""
    return s[0:4] + " " + s[4:8] + " " + s[8:12] + " " + s[12:]


def border_generator():
    """функция возвращает нижнюю границу для генератора карт"""
    low_border = 0
    while len(str(low_border)) < 16:
        low_border = random.randint(0000000000000000, 9999999999999999)
    #    low_border = 0x234f
    return low_border


def card_number_generator(start_: int = 1, finish=9999999999999999) -> str:
    """функция возвращает номера карт из заданного пользователем диапазона"""
    i = start_
    while i < finish:
        yield num_card_formatter(clone(16 - len(str(i))) + str(i))
        i += 1


# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(3):
#    print(next(usd_transactions))


#    descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#       print(next(descriptions))
