import re

regex = r'(ok)(\1\1+)'

text = ("okokokoko okokokokkkkkk")
print([m.group(0) for m in re.finditer(regex, text)])
