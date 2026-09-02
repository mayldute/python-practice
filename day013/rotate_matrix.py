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


def rotate_matrix_v2(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
    current_layer = 0   # current layer: 0 = outside, 1 = one step inside, 2 = two steps inside

    if len(matrix) % 2 != 0:
        center = len(matrix) // 2
        new_matrix[center][center] = matrix[center][center]

    while current_layer < len(matrix) // 2:
        last = len(matrix) - 1 - current_layer  # opposite edge of the current layer

        for col_idx in range(current_layer, last + 1):
            new_matrix[col_idx][last] = matrix[current_layer][col_idx]

        for row_idx in range(current_layer + 1, last):
            new_matrix[last][row_idx] = matrix[- 1 - row_idx][last]

        for col_idx in range(current_layer, last + 1):
            new_matrix[col_idx][current_layer] = matrix[last][col_idx]

        for row_idx in range(current_layer + 1, last):
            new_matrix[current_layer][row_idx] = matrix[- 1 - row_idx][current_layer]

        current_layer += 1

    return new_matrix
