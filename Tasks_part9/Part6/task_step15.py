def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    name = grades['name']
    max_grade = max(grades['grades'])
    return {'name': name, 'top_grade': max_grade}


info = {'name': 'Timur', 'grades': [30, 57, 99]}
print(top_grade(info))