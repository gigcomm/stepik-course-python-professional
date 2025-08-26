def is_good_password(string):
    if len(string) < 9:
        raise LengthError()

    letters = [ch for ch in string if ch.isalpha()]
    if not letters or (all(ch.islower() for ch in letters) or all(ch.isupper() for ch in letters)):
        raise LetterError()

    if not any(ch.isdigit() for ch in string):
        raise DigitError()

    return 'Success!'

found_good = False
while not found_good:
    string = input().strip()
    result = is_good_password(string)
    print(result)

    if result == 'Success!':
        found_good = True
