'''Задание 1:
Напишите функцию для транспонирования матрицы.
Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]'''

def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    '''Транспонирование матрицы'''
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(my_matrix))
