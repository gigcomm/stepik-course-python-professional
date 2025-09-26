import re

regex = r'\b\w*([a-zA-Z])\w*\1\w*\b'

text = ("I have one apple, one banana and one strawberry Priveeeet my dear friend fuisopf gheos, geisslp")
print([m.group(0) for m in re.finditer(regex, text)])
