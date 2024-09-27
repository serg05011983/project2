def get_mask_card_number(card_num_: str) -> str:
    """функция накладывает маску на номер карточки пользователя"""
    card_mask = []
    card_mask.append(card_num_[0:4])
    card_mask.append(card_num_[4:6] + "**")
    card_mask.append("****")
    card_mask.append(card_num_[12:])
    return " ".join(card_mask)


def get_mask_account(mask_num_: str) -> str:
    """функция накладывает маску на номер счёта пользователя"""
    account_mask = "**" + mask_num_[16:]
    return account_mask
