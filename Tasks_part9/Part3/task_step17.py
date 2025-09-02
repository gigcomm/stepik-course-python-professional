# def print_operation_table(operation, rows, cols):
#     for i in range(1, rows + 1):
#         row = []
#         for j in range(1, cols + 1):
#             row.append(str(operation(i,j)))
#         print(' '.join(row))


def print_operation_table(operation, rows, cols):
    table = []
    max_length = 0

    for i in range(1, rows + 1):
        row = []
        for j in range(1, cols + 1):
            value = operation(i, j)
            row.append(value)
            max_length = max(max_length, len(str(value)))
        table.append(row)

    for row in table:
        formatted_row = []
        for value in row:
            formatted_row.append(str(value).rjust(max_length))
        print(' '.join(formatted_row))

print_operation_table(lambda a, b: a * b, 5, 5)