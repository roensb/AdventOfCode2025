
def get_joltage_p1(line):
    first_max = [0,0]
    second_max = [0,0]
    for i, char in enumerate(line[:-1]):
        num = int(char)
        if num > first_max[1]:
            first_max = [i,num]
    for i, char in enumerate(line[first_max[0]+1:]):
        num = int(char)
        if num > second_max[1]:
            second_max = [i,num]

    return int(str(first_max[1])+ str(second_max[1]))

def get_joltage_p2(line, start = 0, step = 12):
    first_max = [0,0]
    if step <= 1:
        search_string = line[start:]
    else:
        search_string = line[start:-step+1]
    for i, char in enumerate(search_string):
        num = int(char)
        if  num > first_max[1]:
            first_max = [start+i,num]
    step -= 1
    if step == 0:
        return first_max[1]
    return int(str(first_max[1]) + str(get_joltage_p2(line,start=first_max[0]+1,step=step)))

def get_total_joltage(filename):
    banks = []
    with open(filename) as f:
        for line in f:
            result = get_joltage_p2(line.strip("\n"))
            banks.append(result)
    return sum(banks)

if __name__ == "__main__":
    print(get_total_joltage("tests/day3.txt"))