def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
            return (value, 'Функция выполнилась без ошибок')
        except Exception:
            return (None, 'При вызове функции произошла ошибка')

    return wrapper


sum = exception_decorator(sum)
print(sum(['199', '1', 187]))

