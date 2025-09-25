import re

regex = r'(bee(geek)+)+'

text = ("beebeegeekgeekgeekbee")
print(*re.findall(regex, text))
