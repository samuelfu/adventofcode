ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

from itertools import groupby
import copy
def split_list_by_delimiter(lst, delimiter):
    return [list(group) for key, group in groupby(lst, lambda x: x != delimiter) if key]

lll = split_list_by_delimiter(ll, '')

print(ll)
def mirror_row(a, b, ll):
    while 0 <= a < len(ll) and 0 <= b < len(ll):
        if ll[a] != ll[b]:
            return False
        a -= 1
        b += 1
    return True

def mirror_col(a, b, ll):
    while 0 <= a < len(ll[0]) and 0 <= b < len(ll[0]):
        for i in range(len(ll)):
            if ll[i][a] != ll[i][b]:
                return False
        a -= 1
        b += 1
    return True

s = 0
reflection_lines = {}
mirror_n = 0
for ll in lll:
    for i in range(len(ll) - 1):
        a, b = i, i + 1
        if mirror_row(a, b, ll):
            print((a + 1) * 100)
            reflection_lines[mirror_n] = (a, b)
            s += (a + 1) * 100
            break
    for j in range(len(ll[0]) - 1):
        a, b = j, j + 1
        if mirror_col(a, b, ll):
            print(a + 1)
            reflection_lines[mirror_n] = (a, b)
            s += a + 1
            break
    mirror_n += 1



def test_mirror(ll, mirror_num):
    for i in range(len(ll) - 1):
        a, b = i, i + 1
        if mirror_row(a, b, ll):
            if reflection_lines[mirror_num] != (a, b):
                print((a + 1) * 100)
                return (a + 1) * 100
    for j in range(len(ll[0]) - 1):
        a, b = j, j + 1
        if mirror_col(a, b, ll):
            if reflection_lines[mirror_num] != (a, b):
                print(a + 1)
                return a + 1
    return 0

s = 0
i = 0
for ll in lll:
    # print(ll)
    r = 0
    for x in range(len(ll)):
        for y in range(len(ll[0])):
            if r > 0:
                continue
            copy_ll = copy.deepcopy(ll)
            if copy_ll[x][y] == '#':
                copy_ll[x] = copy_ll[x][:y] + '.' + copy_ll[x][y+1:]
            else:
                copy_ll[x] = copy_ll[x][:y] + '#' + copy_ll[x][y+1:]
            # print(copy_ll)
            r = test_mirror(copy_ll, i)
            if r > 0:
                s += r

    i += 1



print(s)
