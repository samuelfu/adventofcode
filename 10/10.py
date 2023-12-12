ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

d = {
    ('|', 'UP'): ((-1, 0), 'UP'),
    ('|', 'DOWN'): ((1, 0), 'DOWN'),
    ('-', 'RIGHT'): ((0, 1), 'RIGHT'),  # from west
    ('-', 'LEFT'): ((0, -1), 'LEFT'),
    ('L', 'DOWN'): ((0, 1), 'RIGHT'),  # from north
    ('L', 'LEFT'): ((-1, 0), 'UP'),
    ('J', 'DOWN'): ((0, -1), 'LEFT'),  # from north
    ('J', 'RIGHT'): ((-1, 0), 'UP'),
    ('7', 'UP'): ((0, -1), 'LEFT'),  # from south
    ('7', 'RIGHT'): ((1, 0), 'DOWN'),
    ('F', 'UP'): ((0, 1), 'RIGHT'),  # from south
    ('F', 'LEFT'): ((1, 0), 'DOWN')
}

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            animal = (r, c)

max_loop_dist = 0
found_loop = False
for starting_dx, starting_dy, direction in [(0, 1, 'RIGHT'), (0, -1, 'LEFT'), (1, 0, 'DOWN'), (-1, 0, 'UP')]:
    original_direction = direction
    x, y = animal
    max_dist = 0
    dist = 0
    visited = set()
    while (x, y) not in visited and 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        visited.add((x, y))
        if (x, y) == animal:
            x, y = x + starting_dx, y + starting_dy
        else:
            if (grid[x][y], direction) in d:
                (dx, dy), direction = d[(grid[x][y], direction)]
                x, y = x + dx, y + dy
            else:
                break
        dist += 1
        max_dist = max(max_dist, dist)

    if (x, y) == animal:
        found_loop = True
        max_loop_dist = max(max_loop_dist, max_dist)
        print("Part 1:", max_loop_dist / 2, original_direction)
        break

if original_direction == direction:
    if direction == 'UP' or direction == 'DOWN':
        grid[animal[0]][animal[1]] = '|'
    elif direction == 'LEFT' or direction == 'RIGHT':
        grid[animal[0]][animal[1]] = '-'
else:
    if direction == 'UP' and original_direction == 'RIGHT':
        grid[animal[0]][animal[1]] = 'F'
    elif direction == 'UP' and original_direction == 'LEFT':
        grid[animal[0]][animal[1]] = '7'
    elif direction == 'DOWN' and original_direction == 'RIGHT':
        grid[animal[0]][animal[1]] = 'L'
    elif direction == 'DOWN' and original_direction == 'LEFT':
        grid[animal[0]][animal[1]] = 'J'
    elif direction == 'LEFT' and original_direction == 'DOWN':
        grid[animal[0]][animal[1]] = 'F'
    elif direction == 'RIGHT' and original_direction == 'DOWN':
        grid[animal[0]][animal[1]] = '7'
    elif direction == 'LEFT' and original_direction == 'UP':
        grid[animal[0]][animal[1]] = 'L'
    elif direction == 'RIGHT' and original_direction == 'UP':
        grid[animal[0]][animal[1]] = 'J'

def count(i, j):
    vertical_to_right = 0
    open = False
    for a, b in sorted(visited):
        if a != i or b <= j:
            continue
        # print("visited", "a", a, "b", b, "grid[a][b]", grid[a][b])
        if grid[a][b] == '|':
            vertical_to_right += 1
        elif grid[a][b] == 'F':
            if not open:
                open = True
                prev = 'F'
        elif grid[a][b] == 'L':
            if not open:
                open = True
                prev = 'L'
        elif grid[a][b] == 'J':
            if open:
                if prev == 'F':
                    vertical_to_right += 1
                elif prev == 'L':
                    vertical_to_right += 2
                open = False
            else:
                vertical_to_right += 1
        elif grid[a][b] == '7':
            if open:
                if prev == 'F':
                    vertical_to_right += 2
                elif prev == 'L':
                    vertical_to_right += 1
                open = False
            else:
                vertical_to_right += 1
    #     print("verticle to the right: ", vertical_to_right)
    # print("i", i, "j", j, "verticles", vertical_to_right)
    return vertical_to_right % 2 == 1


area_count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.' or (i, j) not in visited:
            if count(i, j):
                # print("AREA_COUNTED: ", i, j, grid[i][j])
                area_count += 1

print(area_count)

# print(animal)
