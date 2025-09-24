import re

regex = r'<!--.*?-->'

text = " Hi, your tags <!-bee-> and <--geek--> are incorrect. Correct tags look like <!--beegeek--> <!-- header of page --> <-- incorrect header of page !-->"

print(*re.findall(regex, text))