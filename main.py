from src.masks import get_mask_account, get_mask_card_number

while 1:
    account_num = str(input("Введите номер счёта:  "))
    if len(account_num) == 20 and account_num.isdigit():
        break
    else:
        print("Ошибка ввода")

while 1:
    card_num = str(input("Введите номер карты:  "))
    if len(card_num) == 16 and card_num.isdigit():
        break
    else:
        print("Ошибка ввода")

card_example = "1122334455667788"
account_example = "11122233344455566677"

# print(f"Маска карты: {get_mask_card_number(card_num)}")
# print(f"Маска счёта: {get_mask_account(account_num)}")

print(f"Маска карты: {get_mask_card_number(card_example)}")

print(f"Маска счёта: {get_mask_account(account_example)}")
