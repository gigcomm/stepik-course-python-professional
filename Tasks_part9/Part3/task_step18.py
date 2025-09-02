def verification(login, password, success, failure):
    has_any_letter = any(c.isalpha() for c in password)
    has_any_upper = any(c.isupper() for c in password)
    has_any_lower = any(c.islower() for c in password)
    has_any_digit = any(c.isdigit() for c in password)

    if not has_any_letter:
        failure(login, 'в пароле нет ни одной буквы')
        return

    if not has_any_upper:
        failure(login, 'в пароле нет ни одной заглавной буквы')
        return
    if not has_any_lower:
        failure(login, 'в пароле нет ни одной строчной буквы')
        return

    if not has_any_digit:
        failure(login, 'в пароле нет ни одной цифры')

    success(login)

def success(login):
    print(f'Привет, {login}!')
def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')
verification('timyrik20', 'Beegeek314', success, failure)