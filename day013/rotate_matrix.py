"""
Matrix Rotation

Task:
    Rotate a square matrix 90 degrees clockwise.

Requirements:
    - Return the rotated matrix.
    - Handle an empty matrix.
    - Handle a matrix containing a single element.
    - Implement the task in three different ways.
    - Each solution should produce the same result.
"""


def rotate_matrix_v1(matrix: list[list[int]]) -> list[list[int]]:
    col_num = 0
    new_matrix = []

    while col_num < len(matrix):
        new_row = []

        for row in matrix:
            new_row.insert(0, row[col_num])

        new_matrix.append(new_row)
        col_num += 1

    return new_matrix
