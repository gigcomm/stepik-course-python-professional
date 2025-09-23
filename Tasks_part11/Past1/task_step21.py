import re

regex = r'beegeek'

text = "We work really hard in Beegeek =) #python #stepik #beegeek"

print(*re.findall(regex, text))