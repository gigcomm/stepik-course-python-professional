def get_min_max(data: list) -> tuple | None:
    if data is None:
        return None
    max_elem = max(enumerate(data), key=lambda x: x[1])
    min_elem = min(enumerate(data), key=lambda x: x[1])
    return (min_elem[0], max_elem[0])


data = [1, 1, 2, 3, 8, 8]
print(get_min_max(data))
