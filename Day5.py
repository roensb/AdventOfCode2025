import numpy as np
def get_fresh_ingredients_p1(ingredients, ranges):
    total_ingredients = 0
    for r in ranges:
        start,stop = r.split("-")
        start = int(start)
        stop = int(stop)
        start_check = (ingredients - start) >= 0
        stop_check = (stop - ingredients) >= 0
        fresh_ingredients = start_check & stop_check
        fresh_indices = np.where(fresh_ingredients)[0]
        sum_check = fresh_ingredients.sum()
        total_ingredients += sum_check
        ingredients = np.delete(ingredients, fresh_indices)
    return total_ingredients

def parse_file_p1(filename):
    with open(filename, 'r') as f:
        inputs = f.read()
        ranges, ingredients = inputs.split("\n\n")
    ingredients_list = np.array(list(ingredients.split("\n")), dtype=int)
    total_ingredients = get_fresh_ingredients_p1(ingredients_list,ranges.split("\n"))
    return total_ingredients

def get_fresh_ingredients_p2(ranges):
    fresh_ingredients = [list(map(int, s.split("-"))) for s in ranges]
    sorted_fresh_ingredients = sorted(fresh_ingredients)
    merged = []
    for f in sorted_fresh_ingredients:
        if merged and f[0] <= merged[-1][1] <= f[1]:
            merged[-1][1] = f[1]
        elif merged and f[0] >= merged[-1][0] and merged[-1][1] >= f[1]:
            continue
        else:
            merged.append(f)
    total_ingredients = 0
    for r in merged:
        total_ingredients += r[1] - r[0] + 1
    return total_ingredients

def parse_file_p2(filename):
    with open(filename, 'r') as f:
        inputs = f.read()
        ranges, ingredients = inputs.split("\n\n")
    total_ingredients = get_fresh_ingredients_p2(ranges.split("\n"))

    return total_ingredients


if __name__ == "__main__":
    print(parse_file_p2("tests/day5.txt"))