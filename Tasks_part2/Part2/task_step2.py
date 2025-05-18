def get_language(s):
    if 65 <= ord(s) <= 110:
        return 'en'
    elif 1040 <= ord(s) <= 1100:
        return 'ru'
    else:
        return 'unknown'


ru_symbols = "АаВСсЕеНКМОоРрТХху"
en_symbols = "AaBCcEeHKMOoPpTXxy"

symbols = [input().strip() for _ in range(3)]
languages = set(get_language(c) for c in symbols)
if languages == {'ru'}:
    print('ru')
elif languages == {'en'}:
    print('en')
else:
    print('mix')
