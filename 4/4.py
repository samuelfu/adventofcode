from collections import Counter

ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]
num_rows = len(grid)
num_cols = len(grid[0])
import re

print(ll)
res = 0
counter = Counter()
num_scratchcards = 0
for l in range(len(ll)):
    counter[l] += 1
print(counter)
line_number = 0
for l in ll:
    parsed = l.split(':')[1]
    parsed = parsed.split('|')
    official, actual = parsed[0][1:-1], parsed[1][1:]
    numbers = re.findall(r'\d+', official)
    parsed_numbers = list(map(int, numbers))
    official = set(parsed_numbers)
    numbers = re.findall(r'\d+', actual)
    parsed_numbers = list(map(int, numbers))
    actual = set(parsed_numbers)
    while counter[line_number]:
        num_scratchcards += 1
        match_score = 0
        matching_num = 0

        for n in actual:
            if n in official and match_score == 0:
                match_score = 1
                matching_num += 1
            elif n in official and match_score > 0:
                match_score *= 2
                matching_num += 1
        res += match_score
        # print("line", line_number, "before", counter, matching_num)
        for i in range(1, matching_num + 1):
            if line_number + i < len(ll):
                counter[line_number + i] += 1

        counter[line_number] -= 1
    # print("line", line_number, "after", counter, matching_num)
    # print(official, "and",actual)
    line_number += 1

print(res)
# print(counter)
#
# print(sum(counter.values()))
print(num_scratchcards)
# print(num_rows, "rows", num_cols, "cols", grid)