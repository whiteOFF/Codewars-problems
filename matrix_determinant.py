'''
import numpy as np
def determinant(mat):
    return round(np.linalg.det(mat))
'''


def determinant(mat):
    result = 0
    if len(mat) == 1:
        return mat[0][0]
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    for i in range(len(mat)):
        new_mat = [[mat[r][c] for c in range(len(mat)) if c != i] for r in range(1, len(mat))]
        result += (-1) ** i * mat[0][i] * determinant(new_mat)
    return result


print(determinant([[4, 6, 0], [1, 2, 3], [3, 8, 5]]))
