def check_repeated_pattern_concat_v1(s):
    s = str(s)
    if s[int(len(s)/2):] == s[:int(len(s)/2)]:
        return True
    else:
        return False

def check_repeated_pattern_concat_v2(s):
    s = str(s)
    if not s:
        return False
    doubled_s = s + s
    return doubled_s.find(s, 1) != len(s)

def read_input(file_name):
    ranges = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            ranges.extend(line.split(","))
    return ranges

def get_invalid_ids(ranges):
    invalid_ids = []
    for x in ranges:
        start,stop = x.split("-")
        start = int(start)
        stop = int(stop)
        valid = True
        current = start
        while valid:
            if check_repeated_pattern_concat_v2(current):
                invalid_ids.append(current)
            if current == stop:
                valid = False
            current += 1
    return invalid_ids

if __name__ == "__main__":
    ranges = read_input("tests/day2.txt")
    invalid_ids = get_invalid_ids(ranges)
    print(sum(invalid_ids))