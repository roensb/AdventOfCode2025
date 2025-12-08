import numpy as np

def read_file(filename):
    math_matrix = None
    with open(filename, 'r' ) as f:
        for line in f:
            if math_matrix is None:
                math_matrix = np.array(line.split(), dtype=float)
            elif line.split()[0].isdigit():
                math_matrix = np.vstack((math_matrix, np.array(line.split(), dtype=float)))
            else:
                operands = np.array(line.split(), dtype=str)
    return math_matrix, operands

def do_math(math_matrix, operands):
    total = 0
    for i, operand in enumerate(operands):
        match operand:
            case "+":
                total += np.sum(math_matrix[:,i])
            case "*":
                total += np.prod(math_matrix[:,i])
    return total

def read_file_p2(filename):
    with open(filename, 'r' ) as f:
        lines = f.readlines()
        operands = lines.pop(-1).split()
        rotated_lines = []
        for i in zip(*lines):
            rotated_lines.append("".join(i)[::])
    return rotated_lines,operands

def do_math_p2(rotated_lines, operands):
    total = 0
    current_value = 0
    max_len = len(rotated_lines)
    for i, operand in enumerate(operands):
        not_blank = True
        values = np.array([])
        while not_blank:
            if rotated_lines[current_value].strip():
                values = np.append(values, int(rotated_lines[current_value]))
            else:
                not_blank = False
            current_value += 1
            if current_value > max_len-1:
                not_blank = False
        match operand:
            case "+":
                total += np.sum(values)
            case "*":
                total += np.prod(values)
    return total

if __name__ == "__main__":
    matrix,operands = read_file_p2("tests/day6.txt")
    print(do_math_p2(matrix,operands))

