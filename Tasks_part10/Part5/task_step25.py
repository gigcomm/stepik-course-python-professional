def matrix_by_elem(matrix):
    for i in range(len(matrix)):
        yield from matrix[i]



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(*matrix_by_elem(matrix))