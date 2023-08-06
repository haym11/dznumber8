import re
def validate_phone_number(phone_number):
    pattern = r'^(\+)?\d{7,15}$'

    if re.match(pattern, phone_number):
        return True
    else:
        return False

print(validate_phone_number("+380501234567"))
print(validate_phone_number("0501234567"))
print(validate_phone_number("+12345678"))
print(validate_phone_number("123456789012345"))
print(validate_phone_number("abc123"))