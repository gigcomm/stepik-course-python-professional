def sourcetemplate(url):
    def inner(**kwargs):
        if not kwargs:
            return url

        sorted_kwargs = sorted(kwargs.keys())
        query_parts = [f'{key}={kwargs[key]}' for key in sorted_kwargs]
        query = '&'.join(query_parts)
        return f'{url}?{query}'

    return inner

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))

