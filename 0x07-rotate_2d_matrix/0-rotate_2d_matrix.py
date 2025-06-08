#!/usr/bin/python3
""" module for solving the 2D matrix """


def rotate_2d_matrix(matrix):
    """ function to set the algorithm """
    l, r = 0, len(matrix) - 1

    while l < r:
        if i in range(r - l):
            # move counter clockwise to set the new values
            # decraisng the need of new temp pointers
            top, bottom = l, r
            top_left = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = top_left
        r -= 1
        l += 1
