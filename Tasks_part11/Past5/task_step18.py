import re

regex = r'(\b\w+\b)\s+\1\b'

text = ("One can can become a writer only  only if he is   is talented f fa fa")
print([m.group(0) for m in re.finditer(regex, text)])