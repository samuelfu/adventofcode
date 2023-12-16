
ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]
print("first")
print(*[c for c in grid], sep="\n")

def counter_clockwise(m):
    return [list(reversed(col)) for col in zip(*m)]

cycle = 812
# 1 ... 12 ... 23 ... 39 , 40
# 100 would equal to mod 28 = 16
# 4000000000 would equal to mod 28 = 24 - 1
m = {}
total_repeats = 0
for x in range(584):
    if x % 4 == 0:
        if str(grid) not in m:
            m[str(grid)] = x - 1
            total_repeats -= 1
        else:
            print(x - 1, m[str(grid)])
            cycle = x - 1 - m[str(grid)]
            total_repeats += 1
            if total_repeats == 1000:
                break
    # print(*[c for c in grid], sep = "\n")
    # column_grid = grid
    column_grid = []
    for j in range(len(grid[0])):
        c = []
        for i in range(len(grid)):
            c.append(grid[i][j])
        column_grid.append(c)

    for i in range(len(column_grid)):
        for j in range(1, len(column_grid[i])):
            if column_grid[i][j] == 'O':
                k = j - 1
                original = j
                while 0 <= k < j:
                    if column_grid[i][k] == 'O':
                        k += 1
                        break
                    elif column_grid[i][k] == '#':
                        k += 1
                        break
                    elif column_grid[i][k] == '.':
                        k -= 1
                if k < 0:
                    k = 0
                if k != original:
                    column_grid[i][k], column_grid[i][original] = 'O', '.'
            else:
                continue

    normal_grid = []
    for j in range(len(column_grid[0])):
        c = []
        for i in range(len(column_grid)):
            c.append(column_grid[i][j])
        normal_grid.append(c)

    grid = counter_clockwise(normal_grid)

    weight = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                weight += (len(grid) - i)
    print(x, weight)


# normal_grid = []
# for j in range(len(grid[0])):
#     c = []
#     for i in range(len(grid)):
#         c.append(grid[i][j])
#     normal_grid.append(c)

print("final")
print(*[c for c in grid], sep = "\n")
weight = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'O':
            weight += (len(grid) - i)
print(weight)
print("cycle", cycle)