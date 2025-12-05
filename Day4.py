import numpy as np
from scipy.signal import convolve2d
import time

def calculate_adjacent_sum(binary_matrix):
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    adjacent_sums = convolve2d(binary_matrix, kernel, mode='same', boundary='fill', fillvalue=0)
    return adjacent_sums

def get_matrix(filename):
    matrix = None
    with open(filename, 'r') as f:
        for line in f:
            stripped_binary = line.strip("\n").replace(".", "0").replace("@", "1")
            if matrix is None:
                matrix = np.array(list(stripped_binary),dtype=int)
            else:
                matrix = np.vstack((matrix, np.array(list(stripped_binary), dtype=int)))
    return matrix

def sum_matrix(filename):
    matrix = get_matrix(filename)
    adjacent_sums = calculate_adjacent_sum(matrix)
    boolean_matrix = adjacent_sums < 4
    correction = boolean_matrix & matrix
    result = correction.sum()
    return result

def sum_matrix_p2(filename):
    matrix = get_matrix(filename)
    total_removed = 0
    result = None
    while result != 0:
        adjacent_sums = calculate_adjacent_sum(matrix)
        boolean_matrix = adjacent_sums < 4
        correction = boolean_matrix & matrix
        result = correction.sum()
        matrix = np.logical_xor(matrix, correction)
        total_removed += result
    return total_removed

if __name__ == "__main__":
    start = time.time()
    print(sum_matrix_p2("tests/day4.txt"))
    print(start - time.time())