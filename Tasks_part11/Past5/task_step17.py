import re

regex = r'\d{2}(-|---|\.)?\d{2}\1?\d{2}\1?\d{2}'

text = ("I have some groups of digits. Do you want to see? 11-22-33-44 Look at this: 12345678  1-2-3-4-5-6-7-89-w9--99")
print([m.group(0) for m in re.finditer(regex, text)])