import re


def validate_home_phone_number(phone_number):
    pattern = r'^\d{9,10}$'

    if re.match(pattern, phone_number):
        return True
    else:
        return False

print(validate_home_phone_number("123456789"))
print(validate_home_phone_number("9876543210"))
print(validate_home_phone_number("555-123-456"))
print(validate_home_phone_number("12345678901"))
print(validate_home_phone_number("12"))