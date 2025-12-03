from math import floor

def turn_right(current,amount):
    current = current + amount
    clicks = floor(current / 100)
    current = current % 100
    return current, clicks

def turn_left(current, amount):
    if current == 0:
        clicks = -1
    else:
        clicks = 0
    current = current - amount
    if current <= 0:
        clicks = clicks + abs(floor(current / 100))
    current = current % 100
    if current == 0:
        clicks +=1
    return current, clicks

def get_password(file_name, start_value:int):
    with (open(file_name,'r') as f):
        current = int(start_value)
        clicks_count = 0
        for line in f:
            clicks = 0
            value = int(line.strip("\n")[1:])
            if line.startswith('L'):
                current, clicks = turn_left(current,value)
            elif line.startswith('R'):
                current, clicks = turn_right(current,value)
            print(current, clicks)
            clicks_count += clicks
    password = clicks_count
    return password

if "__main__" == __name__:
    print(get_password("tests/test.txt",50))


