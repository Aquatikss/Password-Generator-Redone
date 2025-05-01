import random

def generate_new_password(length, include_upper_case, include_lower_case, include_digits, include_special_chars):
    password = ""

    char_list = ""

    if include_upper_case:
        char_list += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_lower_case:
        char_list += "abcdefghijklmnopqrstuvwxyz"
    if include_digits:
        char_list += "0123456789"
    if include_special_chars:
        char_list += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if not include_upper_case and not include_lower_case and not include_digits and not include_special_chars:
        return "Please select at least one character type."

    if length < 1:
        return "Password length must be at least 1."

    if length > 100:
        return "Password length must be less than or equal to 100."

    for i in range(length):
        password += random.choice(char_list)

    return password