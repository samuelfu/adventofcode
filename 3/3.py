from collections import Counter

ll = [x for x in open('input.txt').read().strip().split('\n')]

def is_special(c):
    if c.isdigit() or c == '.':
        return False
    return True

gear_map = Counter()
number_map = {}

def is_special_near(m, r, i, max_r, max_i):
    search_space = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1))
    contains_special = False
    for x, y in search_space:
        if 0 <= r + x < max_r and 0 <= i + y < max_i:
            if is_special(m[r+x][i+y]):
                contains_special = True
    return contains_special

def get_gear(m, r, i, max_r, max_i):
    search_space = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1))
    gears = []
    for x, y in search_space:
        if 0 <= r + x < max_r and 0 <= i + y < max_i:
            if m[r+x][i+y] == '*':
                gears.append((r+x, i+y))
    return gears

res = 0
m = []
for l in ll:
    r = []
    for c in l:
        r.append(c)
    m.append(r)

for r in range(len(m)):
    row = m[r]
    i = 0
    is_number = False
    connected_to_special = False
    number = ''
    gears = []
    print(row)
    while i < len(row):
        if row[i].isdigit() and not is_number:
            is_number = True
            number += row[i]
            if not connected_to_special and is_special_near(m, r, i, len(m), len(row)):
                connected_to_special = True
            gears.extend(get_gear(m, r, i, len(m), len(row)))
        elif row[i].isdigit() and is_number:
            number += row[i]
            if not connected_to_special and is_special_near(m, r, i, len(m), len(row)):
                connected_to_special = True
            gears.extend(get_gear(m, r, i, len(m), len(row)))
        elif not row[i].isdigit() and not is_number:
            i += 1
            continue
        elif not row[i].isdigit() and is_number:
            is_number = False
            if connected_to_special:
                res += int(number)
                # print(number)
            print(gears)
            for x, y in set(gears):
                gear_map[(x, y)] += 1
                if (x, y) in number_map:
                    number_map[(x, y)] *= int(number)
                else:
                    number_map[(x, y)] = int(number)
            connected_to_special = False
            number = ''
            gears = []

        i += 1
        if i == len(row) and is_number:
            if connected_to_special:
                res += int(number)
                # print(number)
            print(gears)
            for x, y in set(gears):
                gear_map[(x, y)] += 1
                if (x, y) in number_map:
                    number_map[(x, y)] *= int(number)
                else:
                    number_map[(x, y)] = int(number)
            is_number = False
            connected_to_special = False
            number = ''
            gears = []


# print(res)
gear_ratio = 0
for x, y in gear_map:
    if gear_map[(x, y)] == 2:
        gear_ratio += number_map[(x, y)]

print(gear_map)
print(number_map)
print(gear_ratio)
