def spell(*args):
    result_dict = {}
    for word in args:
        first_letter = word[0].lower()
        if first_letter not in result_dict or len(word) > result_dict[first_letter]:
            result_dict[first_letter] = len(word)
    return result_dict

words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай',
'УЗБЕКИСТАН']
print(spell(*words))
