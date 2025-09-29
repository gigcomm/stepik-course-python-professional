import re
from re import escape


def multiple_split(string, delimiters):
    escape_delim = [re.escape(d) for d in delimiters]
    pattern = re.compile('|'.join(escape_delim))
    result = re.split(pattern, string)
    return result


print(multiple_split('beegeek-python.stepik', ['.', '-']))
print(multiple_split('Timur---Arthur+++Dima****Anri', ['---', '+++', '****']))
print(multiple_split('timur.^[+arthur.^[+dima.^[+anri.^[+roma.^[+ruslan',['.^[+']))