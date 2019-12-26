import numpy as np

from . import functions


def from_string(coordinates_str):
    coordinates_str = coordinates_str.split(';')
    coordinates = []
    for s in coordinates_str:
        s = s.split(',')
        coordinates.append(s)
    coordinates = np.array(coordinates, dtype=np.float)
    matrix = create_matrix(coordinates)
    values = gaussian_elimination(matrix)
    return create_function(values)


def create_matrix(coordinates):
    matrix = []
    for coordinate in coordinates:
        matrix.append(create_matrix_row(coordinate, len(coordinates)))
    return np.array(matrix, dtype=np.float)


def create_matrix_row(coordinate, n):
    row = []
    for i in range(n - 1, -1, -1):
        row.append(coordinate[0] ** i)
    row.append(coordinate[1])
    return row


def create_function(values):
    terms = []
    for index, item in enumerate(values):
        terms.append(
            functions.ProductFunction(
                functions.RealNumberFunction(item),
                functions.PowerFunction(
                    functions.VariableFunction(),
                    functions.NaturalNumberFunction((len(values) - 1) - index)
                )
            )
        )
    return functions.sum_all(terms)


def gaussian_elimination(matrix):
    row_count, column_count = matrix.shape
    assert column_count == row_count + 1, 'Matrix not in the right size'

    for h in range(row_count):
        max_i = np.argmax([np.abs(matrix[i, h]) for i in range(h, row_count)]) + h

        assert matrix[max_i, h] != 0, 'Matrix is singular!'

        matrix[[max_i, h]] = matrix[[h, max_i]]

        for i in range(h + 1, row_count):
            f = matrix[i, h] / matrix[h, h]
            for j in range(h + 1, column_count):
                matrix[i, j] -= matrix[h, j] * f
            matrix[i, h] = 0

    x = []
    for i in range(row_count - 1, -1, -1):
        x.insert(0, matrix[i, row_count] / matrix[i, i])
        for h in range(i - 1, -1, -1):
            matrix[h, row_count] -= matrix[h, i] * x[0]
    return np.array(x, dtype=np.float)


if __name__ == '__main__':
    # A = np.array([[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]], dtype=np.float)
    # B = np.array([[-27, 9, -3, 1, -1], [-8, 4, -2, 1, 0], [-1, 1, -1, 1, -1], [0, 0, 0, 1, 2]], dtype=np.float)
    # s = gaussian_elimination(B)
    # print(s)
    f = from_string('-3,-1;-2,0;-1,-1;0,2')
    print(f)
