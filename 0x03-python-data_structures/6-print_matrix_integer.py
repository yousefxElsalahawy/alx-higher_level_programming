#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for j, y in enumerate(x):
            print("{:d}".format(y), end = " " if j != len(x)-1 else "\n" )
