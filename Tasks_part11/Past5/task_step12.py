import re

regex = r'([a-z])([a-zA-Z_\d])([A-Z])\1\2\3'

text = ("Hello, User211, your verification number: z5Az5A")
print([m.group(0) for m in re.finditer(regex, text)])
