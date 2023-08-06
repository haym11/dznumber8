import re


def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.[\w]{2,}$'

    if re.match(pattern, email):
        return True
    else:
        return False

print(validate_email("example@gmail.com"))
print(validate_email("user@domain.co.uk"))
print(validate_email("user.name@company.com"))
print(validate_email("invalid_email.com"))
print(validate_email("user@invalid_domain."))
print(validate_email("very_long_username_with_many_characters@example.com"))  