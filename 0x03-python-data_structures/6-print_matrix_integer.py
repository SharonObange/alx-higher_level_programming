#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    index = 0
    for row in matrix:
        for x in row:
            print("{:d}".format(x), end=" ")
            index += 1
        print()
