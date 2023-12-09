ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

# the lowest location number that corresponds to any of the initial seeds
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.


seeds = ll[0].split(':')[1].strip().split()
i = 1
type_map = {
0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]
}
type = -1
while i < len(ll):
    if ll[i] == '':
        i += 1
        type += 1
    else:
        while i < len(ll):
            i += 1
            if i == len(ll) or ll[i] == '':
                break
            locs = ll[i].split()
            type_map[type].append([int(locs[0]), int(locs[1]), int(locs[2])])

print(type_map)
m = float('inf')
# for origin in range(loc_s, loc_s + loc_r):
for origin in range(261668924//4):
    current_origin = origin
    # print(current_origin)
    for i in reversed(range(len(type_map) - 1)):
        current_ranges = type_map[i]
        for d, s, r in current_ranges:
            # print(d, s, r)
            if current_origin in range(d, d + r):
                # print(current_origin, current_origin + s - d)
                current_origin = current_origin + s - d
                break

    # print("final:", current_origin, origin)
    s = 0
    while s < len(seeds):
        if current_origin in range(int(seeds[s]), int(seeds[s]) + int(seeds[s+1])):
            m = min(m, origin)
        s += 2
print(m)
# print(ll)
