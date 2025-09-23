text = input()

def is_format1(phone: str) -> bool:
    parts = phone.split('-')
    if len(parts) != 5:
        return False
    if not phone.startswith("7-"):
        return False
    return all(part.isdigit() for part in parts[1:]) and all(len(p) in (2,3) for p in parts[1:])

def is_format2(phone: str) -> bool:
    parts = phone.split('-')
    if len(parts) != 4:
        return False
    if not phone.startswith("8-"):
        return False
    return all(part.isdigit() for part in parts[1:]) and all(len(p) in (3,4) for p in parts[1:])

def get_all_numbers(text):
    for i in range(len(text)):
        chunk15 = text[i:i+15]
        chunk14 = text[i:i+14]
        if is_format1(chunk15):
            yield chunk15
        if is_format2(chunk14):
            yield chunk14

print(*get_all_numbers(text), sep="\n")
