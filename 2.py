from collections import Counter

# part 1
ll = [x for x in open('2.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

report = [p.split() for p in ll]
report = [[int(level) for level in r] for r in report]

result = []
for level in report:
    ascending = None
    level_result = True
    for i in range(1, len(level)):
        if level[i] > level[i-1] and ascending is None:
            ascending = True
        elif level[i] < level[i-1] and ascending is None:
            ascending = False
        elif level[i] > level[i-1] and not ascending:
            level_result = False
        elif level[i] < level[i-1] and ascending:
            level_result = False
        if 3 < abs(level[i] - level[i-1]) or abs(level[i] - level[i-1]) < 1:
            level_result = False
    result.append(level_result)

print(sum(result))

# part 2

result = []
for level in report:
    ascending = None
    level_result = True
    tolerance = True
    for i in range(1, len(level)):
        if level[i] > level[i-1] and ascending is None:
            ascending = True
        elif level[i] < level[i-1] and ascending is None:
            ascending = False
        elif level[i] > level[i-1] and not ascending:
            if tolerance:
                tolerance = False
            else:
                level_result = False
        elif level[i] < level[i-1] and ascending:
            if tolerance:
                tolerance = False
            else:
                level_result = False
        if 3 < abs(level[i] - level[i-1]) or abs(level[i] - level[i-1]) < 1:
            if tolerance:
                tolerance = False
            else:
                level_result = False
    result.append(level_result)

print(sum(result))