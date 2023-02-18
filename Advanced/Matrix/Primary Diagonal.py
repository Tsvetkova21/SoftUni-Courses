def read_matrix_func():
    number_of_rows= int(input())
    current_matrix = []
    for row in range(number_of_rows):
        row_data = list(map(int, input().split(' ')))
        current_matrix.append(row_data)
    return current_matrix

def primary_diagonal():
    matrix = read_matrix_func()
    rows = len(matrix)
    columns = len(matrix[0])
    sum_primary = 0

    for i in range(rows):
        for j in range(columns):
            if i == j:
                sum_primary+=matrix[i][j]
    return sum_primary

print(primary_diagonal())