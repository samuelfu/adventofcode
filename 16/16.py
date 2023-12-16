ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

d = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "RIGHT": (0, 1),
    "LEFT": (0, -1),
}

max_energized = 0
for starting_direction in ('RIGHT', 'LEFT'):
    for i in range(len(grid)):
        visited = set()
        j = 0 if starting_direction == 'RIGHT' else len(grid[0]) - 1
        beams = [((i, j), starting_direction)]
        # print(beams)

        while beams:
            b = beams.pop()
            (x, y), direction = b
            if b in visited or x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            if direction in ('RIGHT', 'LEFT'):
                if grid[x][y] == '|':
                    beams.append(((x - 1, y), "UP"))
                    beams.append(((x + 1, y), "DOWN"))
                elif grid[x][y] == '-' or grid[x][y] == '.':
                    dx, dy = d[direction]
                    beams.append(((x + dx, y + dy), direction))
                elif grid[x][y] == '/':
                    if direction == 'RIGHT':
                        beams.append(((x - 1, y), "UP"))
                    else:
                        beams.append(((x + 1, y), "DOWN"))
                elif grid[x][y] == '\\':
                    if direction == 'LEFT':
                        beams.append(((x - 1, y), "UP"))
                    else:
                        beams.append(((x + 1, y), "DOWN"))
            elif direction in ('UP', 'DOWN'):
                if grid[x][y] == '-':
                    beams.append(((x, y - 1), "LEFT"))
                    beams.append(((x, y + 1), "RIGHT"))
                elif grid[x][y] == '|' or grid[x][y] == '.':
                    dx, dy = d[direction]
                    beams.append(((x + dx, y + dy), direction))
                elif grid[x][y] == '/':
                    if direction == 'UP':
                        beams.append(((x, y + 1), "RIGHT"))
                    else:
                        beams.append(((x, y - 1), "LEFT"))
                elif grid[x][y] == '\\':
                    if direction == 'DOWN':
                        beams.append(((x, y + 1), "RIGHT"))
                    else:
                        beams.append(((x, y - 1), "LEFT"))

            visited.add(((x, y), direction))
            # print(b, beams[-1])

        for r in range(len(grid)):
            s = ''
            for c in range(len(grid[0])):
                if ((r, c), 'RIGHT') in visited or ((r, c), 'LEFT') in visited or ((r, c), 'UP') in visited or ((r, c), 'DOWN') in visited:
                    s += '#'
                else:
                    s += '.'
            # print(s)

        # print(visited)
        # print(len(set([(x,y) for (x,y), d in visited])))
        max_energized = max(max_energized, len(set([(x,y) for (x,y), d in visited])))

for starting_direction in ('UP', 'DOWN'):
    for j in range(len(grid[0])):
        visited = set()
        i = 0 if starting_direction == 'DOWN' else len(grid) - 1
        beams = [((i, j), starting_direction)]
        # print(beams)

        while beams:
            b = beams.pop()
            (x, y), direction = b
            if b in visited or x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            if direction in ('RIGHT', 'LEFT'):
                if grid[x][y] == '|':
                    beams.append(((x - 1, y), "UP"))
                    beams.append(((x + 1, y), "DOWN"))
                elif grid[x][y] == '-' or grid[x][y] == '.':
                    dx, dy = d[direction]
                    beams.append(((x + dx, y + dy), direction))
                elif grid[x][y] == '/':
                    if direction == 'RIGHT':
                        beams.append(((x - 1, y), "UP"))
                    else:
                        beams.append(((x + 1, y), "DOWN"))
                elif grid[x][y] == '\\':
                    if direction == 'LEFT':
                        beams.append(((x - 1, y), "UP"))
                    else:
                        beams.append(((x + 1, y), "DOWN"))
            elif direction in ('UP', 'DOWN'):
                if grid[x][y] == '-':
                    beams.append(((x, y - 1), "LEFT"))
                    beams.append(((x, y + 1), "RIGHT"))
                elif grid[x][y] == '|' or grid[x][y] == '.':
                    dx, dy = d[direction]
                    beams.append(((x + dx, y + dy), direction))
                elif grid[x][y] == '/':
                    if direction == 'UP':
                        beams.append(((x, y + 1), "RIGHT"))
                    else:
                        beams.append(((x, y - 1), "LEFT"))
                elif grid[x][y] == '\\':
                    if direction == 'DOWN':
                        beams.append(((x, y + 1), "RIGHT"))
                    else:
                        beams.append(((x, y - 1), "LEFT"))

            visited.add(((x, y), direction))
            # print(b, beams[-1])

        for r in range(len(grid)):
            s = ''
            for c in range(len(grid[0])):
                if ((r, c), 'RIGHT') in visited or ((r, c), 'LEFT') in visited or ((r, c), 'UP') in visited or ((r, c), 'DOWN') in visited:
                    s += '#'
                else:
                    s += '.'
            # print(s)

        # print(visited)
        # print(len(set([(x,y) for (x,y), d in visited])))
        max_energized = max(max_energized, len(set([(x,y) for (x,y), d in visited])))

print(max_energized)