# Course: CS261 - Data Structures
# Student Name: Holly Murray
# Assignment: Homework1 Problem 3
# Description: This program sums two matrices of the same dimensions and returns the resulting matrix.
# If the dimensions of the two matrices are not equal it returns 'None'

# This function sums two matrices and returns the resulting matrix
def matrix_add(a: [[]], b: [[]]) -> [[]]:
    """    TODO: Write this implementation    """
    # DIMENSIONS CHECK

    # dimensions are equal
    if dimCheck(rowsCount(a),rowsCount(b),colsCount(a),colsCount(b)) == True:

        rows = rowsCount(a)
        cols = colsCount(a)
        matrix = [[0] * cols for _ in range(rows)]
        trows = 0

        while trows < rows:
            tcols = 0
            while tcols < cols:
                matrix[trows][tcols] = a[trows][tcols] + b[trows][tcols]
                tcols += 1
            trows += 1
    # dimensions are not equal, return none
    else:
        return "None"
    return matrix


# Receives a matrix and returns the number of rows
def rowsCount(matrix: [[]]) -> int:
    count = 0
    for i in matrix:
        count = count + 1
    return count

# Receives a matrix and returns the number of columns
def colsCount(matrix: [[]]) -> int:
    count = 0
    for i in matrix:
        for j in i:
            count = count+1
        return count

# Receives a four integers that represent the columns and rows of two matrices.
# It then checks to make sure the rows and dimensions are the same
def dimCheck(rows1: int, rows2: int, cols1: int, cols2: int) -> bool:
    if rows1 == rows2:
        if cols1 == cols2:
            return True
    else:
        return False

# BASIC TESTING
if __name__ == "__main__":
    # example 1
    m1 = [[1, 2, 3], [2, 3, 4]]
    m2 = [[5, 6, 7], [8, 9, 10]]
    m3 = [[1, 2], [3, 4], [5, 6]]


    print(matrix_add(m1, m2))
    print(matrix_add(m1, m3))
    print(matrix_add(m1, m1))
    print(matrix_add([[]], [[]]))
    print(matrix_add([[]], m1))