def is_good_password(string):
    if len(string) < 9:
        raise LengthError()

    letters = [ch for ch in string if ch.isalpha()]
    if not letters or (all(ch.islower() for ch in letters) or all(ch.isupper() for ch in letters)):
        raise LetterError()

    if not any(ch.isdigit() for ch in string):
        raise DigitError()

    return True
