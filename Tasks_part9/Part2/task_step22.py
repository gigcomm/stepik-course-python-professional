func_str = input().strip()
a, b = map(int, input().split())

values = [eval(func_str) for x in range(a, b + 1)]

print(f"Минимальное значение функции {func_str} на отрезке [{a}; {b}] равно {min(values)}")
print(f"Максимальное значение функции {func_str} на отрезке [{a}; {b}] равно {max(values)}")
