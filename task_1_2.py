'''
Задание №1
Напишите функцию для транспонирования матрицы
'''

matrix = [[2, 4, 6, 8],
          [3, 5, 7, 9]]
print("исходная матрица:\n", matrix)

def matrix_transposition(matrix):
    trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print(trans_matrix)
print("транспонированная матрица:")
matrix_transposition(matrix)