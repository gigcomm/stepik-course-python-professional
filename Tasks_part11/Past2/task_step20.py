import re

regex = r'\+7\d{10}|\+7\(\d{3}\)\d{7}|\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}|\+7 \d{3} \d{3} \d{2} \d{2}'

text = "Home: +7 927 991 13 31 Work: +7(917)-634-81-19 Alice: +89119873582 Arthur: +7(987)6639481 Timur: +79176879054"

print(*re.findall(regex, text))