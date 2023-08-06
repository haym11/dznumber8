import re

def validate_full_name(full_name):
    pattern = r'^\w{2,20}\s\w{2,20}\s\w{2,20}$'

    if re.match(pattern, full_name):
        return True
    else:
        return False

print(validate_full_name("John Doe Smith"))
print(validate_full_name("Ann"))
print(validate_full_name("ThisNameIsTooLongToBeAccepted"))
print(validate_full_name("Mary Johnson"))
print(validate_full_name("John 123 Smith"))  