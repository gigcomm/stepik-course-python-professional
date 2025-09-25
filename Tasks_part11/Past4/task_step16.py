import re

regex = r'^[A-Za-z02468]{40}[13579| ]{5}$'

text = ("BpOBNpqKg4EgPKxWn8wavcQMOP06nbCwvOdu6CPj11111")

print(*re.findall(regex, text))
