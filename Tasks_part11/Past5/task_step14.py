
import re

regex = r'(.)(.)(.)(.)(.)\4\3\2\1'

text = ("What is palindrome? Examples: -._.-._.-, rotavator, abba, deleveled, 123454321  a1.-B-.1a")
print([m.group(0) for m in re.finditer(regex, text)])
