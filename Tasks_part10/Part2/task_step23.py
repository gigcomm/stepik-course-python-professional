from typing import Iterable


def get_min_max(iterable: Iterable) -> tuple | None:
    if iterable is None:
        return None
    items = list(iterable)
    min_elem = min(items)
    max_elem = max(items)
    return min_elem, max_elem

iterable = iter(range(10))
print(get_min_max(iterable))