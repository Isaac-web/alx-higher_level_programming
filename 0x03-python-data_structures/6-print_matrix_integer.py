#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
  if matrix is None:
    return
  for line in matrix:
    for element in line:
      print(" {}".format(element), end="")
    print("")
