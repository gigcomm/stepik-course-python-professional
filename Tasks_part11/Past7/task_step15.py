import re


def abbreviate(phrase):
    match = re.findall(r'\b\w|[A-Z]', phrase)
    return ''.join(match).upper()

print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))
print(abbreviate('JS game sec'))