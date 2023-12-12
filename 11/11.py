from itertools import combinations

ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

rows_without_galaxy = []
columns_without_galaxy = []
galaxies = []
for i in range(len(grid)):
    no_galaxy = True
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            no_galaxy = False
            galaxies.append((i,j))

    if no_galaxy:
        rows_without_galaxy.append(i)

for j in range(len(grid[0])):
    no_galaxy = True
    for i in range(len(grid)):
        if grid[i][j] == '#':
            no_galaxy = False

    if no_galaxy:
        columns_without_galaxy.append(j)

galaxy_pairs = list(combinations(galaxies, 2))
res = 0
for (x1, y1), (x2, y2) in galaxy_pairs:
    dist = abs(y1 - y2) + abs(x1 - x2)
    for r in rows_without_galaxy:
        if x1 < r < x2 or x2 < r < x1:
            dist += 999999
    for c in columns_without_galaxy:
        if y1 < c < y2 or y2 < c < y1:
            dist += 999999
    res += dist
    print(dist)
print(res)
