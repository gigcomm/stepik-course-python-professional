import re

regex = r'\b[A-Z]\w*\b'

text = ("I signed up in the app using my Apple ID. How can I sign in to the web version?")

print(*re.findall(regex, text))
