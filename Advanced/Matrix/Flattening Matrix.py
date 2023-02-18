#matrix = [[int(el) for el in input().split(", ")] for _ in range (int(input()))]
matrix = []
n = int(input())
for row in range(n):
    row_data = list(map(int, input().split(', ')))
    matrix.append(row_data)
#result =[num for row in matrix for num in row]
#print(result)

new_matrix = []
for row in matrix:
    for num in row:
        new_matrix.append(num)
print(new_matrix)