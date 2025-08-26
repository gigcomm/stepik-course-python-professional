def is_good_password(string):
    if len(string) < 9:
        return False

    has_lower = False
    has_upper = False
    has_digit = False

    for ch in string:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
    if has_lower and has_upper and has_digit:
        return True
    return False

print(is_good_password('МойПарольСамыйЛучший111'))