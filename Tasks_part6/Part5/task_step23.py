from collections import defaultdict


def flip_dict(dict_of_lists):
    result_flip_dict = defaultdict(list)
    for key, value in dict_of_lists.items():
        for item in value:
            result_flip_dict[item].append(key)
    return result_flip_dict


data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'],
'Anri': ['juice', 'coffee']}
for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')