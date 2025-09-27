import re

article = """Stepik is a great platform for learning Python.
I love coding...
stepik provides interactive courses!
Today is a sunny day.
STEPiK offers free courses...
Learning is fun!"""

print(len(re.findall('^Stepik.*', article, re.IGNORECASE | re.MULTILINE)))
print(len(re.findall(r"\.\.\.|!$", article, re.MULTILINE)))




