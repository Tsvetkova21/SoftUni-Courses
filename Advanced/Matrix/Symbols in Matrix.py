def read_matrix_func():
    number_of_rows= int(input())
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(input())
        current_matrix.append(row_data)
    return current_matrix

def check_special_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            current_element = matrix[row][col]
            if current_element==symbol:
                return row,col

def print_fun(data, symbol):
    if data:
        print(data)
    else:
        print(f'{symbol} does not occur in the matrix')

matrix = read_matrix_func()
special_symbol = input()
print_fun(check_special_symbol(matrix,special_symbol),special_symbol)

