#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for _, x in enumerate(matrix):
        for j, y in enumerate(x):
            print("{:d}".format(y), end = " " if j != len(x)-1 else "$" )
        print("")
