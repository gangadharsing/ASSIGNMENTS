# 7. Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
# Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
# Original Matrix: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

def matrix(M):
    result = sorted(M, key=lambda matrix_row: sum(matrix_row))
    return result
matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print("Original Matrix:")
print(matrix1)
print("Sort the matrix in ascending order according to the sum of its rows")
print(matrix(matrix1))
print("Original Matrix:")
print(matrix2)
print("Sort the matrix in ascending order according to the sum of its rows")
print(matrix(matrix2))


