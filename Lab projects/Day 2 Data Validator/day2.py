import validators
import datetime


def valid_email(email_for_check):
    if not validators.email(email_for_check):
        return False
    return True


def valid_url(url_for_check):
    if not validators.url(url_for_check):
        return False
    return True


def valid_date(date_for_check):
    try:
        datetime.datetime.strptime(date_for_check, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def valid_number(number_for_check):
    try:
        complex(number_for_check)
        return True
    except:
        return False


def valid_card_number(card_number_for_check):
    if 8 <= len(card_number_for_check) <= 19 and card_number_for_check.isnumeric():
        return True
    return False


def valid_phone_number(phone_number_for_check):
    if (phone_number_for_check[:5] == "+374" or len(phone_number_for_check) == 12) or \
            (phone_number_for_check[0] == "0" or len(phone_number_for_check) == 9):
        if phone_number_for_check[1:].isnumeric():
            return True
    return False


to_val = input("what to validate ")
val = input("your input ")
if to_val == "Email":
    print(valid_email(val))
elif to_val == "URL":
    print(valid_url(val))
elif to_val == "Date":
    print(valid_date(val))
elif to_val == "Number":
    print(valid_number(val))
elif to_val == "Card Number":
    print(valid_card_number(val))
elif to_val == "Phone Number":
    print(valid_phone_number(val))
