'''
Задание №1
Напишите функцию для транспонирования матрицы
'''

matrix = [[2, 4, 6, 8],
          [3, 5, 7, 9]]
print("исходная матрица:\n", matrix)
def matrix_transposition(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]  # структура транспонированной матцы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)
print("транспонированная матрица:")
matrix_transposition(matrix)
