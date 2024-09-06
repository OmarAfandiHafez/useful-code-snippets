import re


def validate_egyptian_phone_number(phone_number):
    regx = '^(00201|201|\+201|01|1)(0|1|2|5)([0-9]{8})$'
    return bool(re.match(regx, phone_number))


def validate_saudi_phone_number(phone_number):
    regx = '^(009665|9665|\+9665|05|5)(0|3|4|5|6|7|8|9)([0-9]{7})$'
    return bool(re.match(regx, phone_number))

