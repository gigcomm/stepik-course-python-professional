import keyword
import re

text = input().strip()
list_keyword = keyword.kwlist
pattern = r'\b(' + '|'.join(re.escape(kw) for kw in list_keyword) + r')\b'
res = re.sub(pattern, r'<kw>', text, flags=re.I)
print(res)

