from typing import Union


def filter_by_state(
    spisok_data_: Union[list[dict[str, int]]], state_: str = "EXECUTED"
) -> list[dict[str, int]]:
    """Функция выполняет фильтрацию данных по принимаемому ключу"""
    spisok_data_filtered = []
    for dat in spisok_data_:
        if dat.get("state") == state_:
            spisok_data_filtered.append(dat)
    return spisok_data_filtered


def sort_by_date(
    spisok_data_: Union[list[dict[str, int]]], reverse_: bool = True
) -> list[dict[str, int]]:
    """Функция выполняет сортировку принимаемого списка словарей по дате"""
    sorted_spisok = sorted(
        spisok_data_, key=lambda spisok_data_: spisok_data_["date"], reverse=reverse_
    )
    return sorted_spisok


spisok_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(spisok_data, "EXECUTED"))
print(filter_by_state(spisok_data, "CANCELED"))
print(filter_by_state(spisok_data))
print(sort_by_date(spisok_data, True))
print(sort_by_date(spisok_data, False))
print(sort_by_date(spisok_data))
