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

def beam_me(matrix):
    total_splits = 0
    max_matrix = len(matrix)
    for i, row in enumerate(matrix):
        if i+1 == max_matrix:
            break
        print(row)
        new_row = row + matrix[i+1]
        print(new_row)
        splits = new_row > 2
        total_splits += np.sum(splits)
        locations = np.where(splits)
        new_row[new_row == 2] = 0
        new_row[new_row > 2] = 2
        for location in locations:
            if location.size == 0:
                break
            if new_row[location[0]+ 1] < 1:
                new_row[location[0]+ 1] = 1
            if new_row[location[0]- 1] < 1:
                new_row[location[0]- 1] = 1
        matrix[i+1] = new_row
    return total_splits

if __name__ == "__main__":
    print(beam_me(read_file("tests/day7.txt")))