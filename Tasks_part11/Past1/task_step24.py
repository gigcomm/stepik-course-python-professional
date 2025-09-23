import re

regex = r'\d{3}-\d{3}-\d{4}'

text =  "Sample Input 1: Call me tonight: 415-441-9116, xxx-xxx-xx37"

print(*re.findall(regex, text))