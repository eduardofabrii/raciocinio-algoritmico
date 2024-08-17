# 9. Crie um programa que leia uma matriz de ordem n (números inteiros) e calcule a soma dos elementos abaixo da diagonal principal. Ou seja, a soma dos elementos a_ij com i > j.
n = int(input("Enter the order of the matrix: "))

matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Enter the element at position ({i}, {j}): "))
        row.append(element)
    matrix.append(row)

sum_below_diagonal = 0
for i in range(n):
    for j in range(i):
        sum_below_diagonal += matrix[i][j]

print("Sum of elements below the diagonal:", sum_below_diagonal)
# Calculate the sum of elements below the diagonal
sum_below_diagonal = sum(matrix[i][j] for i in range(n) for j in range(i))

print("Sum of elements below the diagonal:", sum_below_diagonal)