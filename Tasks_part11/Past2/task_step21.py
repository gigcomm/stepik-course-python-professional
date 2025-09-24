import re

regex = (r'\d{2}[./]\d{2}[./]\d{4}|\d{4}[./]\d{2}[./]\d{2}')

text = "-- Exam days -- Math: 24.03.2022 Chemistry: 24/03/2022 Physics: 2022.03.25 France: 2022/03/29"

print(*re.findall(regex, text))