import string

mapping = input().strip()
text = input()

lower_trans = str.maketrans(string.ascii_lowercase, mapping)
upper_trans = str.maketrans(string.ascii_uppercase, mapping)

translated = text.translate(lower_trans).translate(upper_trans)
print(translated)
