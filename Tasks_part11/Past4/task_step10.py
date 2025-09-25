import re

regex = r'\b[aA]n?\b'

text = ("A cow is an animal. I have been reading this text for aN hour. Сan you give me this book? "
        "AN or an apple  An acle, a Ancle, A antarktida, an Any")

print(*re.findall(regex, text))
