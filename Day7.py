import numpy as np

def read_file(filename):
    matrix = None
    with open(filename, 'r') as f:
        for line in f:
            stripped_line = line.strip().replace("S", "1").replace(".","0").replace("^","2")
            if matrix is None:
                matrix = np.array(list(stripped_line), dtype=int)
            else:
                matrix = np.vstack((matrix, np.array(list(stripped_line), dtype=int)))
    return matrix

def beam_me_p1(matrix):
    total_splits = 0
    max_matrix = len(matrix)
    for i, row in enumerate(matrix):
        if i+1 == max_matrix:
            break
        new_row = row + matrix[i+1]
        splits = new_row == 3
        total_splits += np.sum(splits)
        locations = np.where(splits)
        new_row[new_row == 2] = 0
        new_row[new_row > 2] = 2
        for location in locations[0]:
            if new_row[location+ 1] < 1:
                new_row[location+ 1] = 1
            if new_row[location- 1] < 1:
                new_row[location- 1] = 1
        matrix[i+1] = new_row
    return total_splits, matrix

def beam_me_p2(matrix):
    total_splits = 0
    max_matrix = len(matrix)
    for i, row in enumerate(matrix):

        if i+1 == max_matrix:
            break
        new_row = row + matrix[i+1].copy()
        splits = new_row == 3
        total_splits += np.sum(splits)
        locations = np.where(splits)
        new_row[new_row == 2] = 0
        new_row[new_row > 2] = 2
        if i == 0:
            paths_matrix = np.array([row.copy()])
        else:
            stack = paths_matrix[-1].copy()
            paths_matrix = np.vstack((paths_matrix, stack))
        if all(a.size == 0 for a in locations):
            paths_matrix[-1] = paths_matrix[i]
        for location in locations[0]:
            if new_row[location+ 1] <= 1:
                new_row[location+ 1] = 1
                paths_matrix[-1][location+ 1] += paths_matrix[i][location]
            if new_row[location- 1] <= 1:
                new_row[location - 1] = 1
                paths_matrix[-1][location- 1] +=  paths_matrix[i][location]
            paths_matrix[-1][location] = 0
        matrix[i+1] = new_row
    return np.sum(paths_matrix[-1])



if __name__ == "__main__":
    print(beam_me_p2(read_file("tests/day7.txt")))