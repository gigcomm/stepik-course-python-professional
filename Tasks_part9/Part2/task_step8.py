def hash_as_key(objects):
    result = {}
    for obj in objects:
        hashed = hash(obj)
        if hashed in result:
            if isinstance(result[hashed], list):
                result[hashed].append(obj)
            else:
                result[hashed] = [result[hashed], obj]
        else:
            result[hashed] = obj
    return result

data = [-1, -2, -3, -4, -5]
print(hash_as_key(data))