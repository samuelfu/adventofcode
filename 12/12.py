from functools import cache

ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

springs = []
configs = []
for l in ll:
    s = l.split()
    new_spring = (s[0] + '?') * 1
    springs.append(new_spring[:-1])
    new_config = (s[1] + ',') * 1
    new_config = tuple(int(x) for x in new_config[:-1].split(','))
    configs.append(new_config)

print(springs, tuple(configs))

c = {}
@cache
def calculate(input_string, input_config):
    print(input_string, input_config)
    if not input_config:
        return 1
    if not input_string:
        return 0

    c = 0
    for i in range(len(input_string)):
        if input_string[i] == '?':
            hot_spring_config = list(input_config[:])
            hot_spring_config[0] -= 1
            if hot_spring_config[0] == 0:
                hot_spring_config = hot_spring_config[1:]
            hot_spring_version = calculate(input_string[i+1:], tuple(hot_spring_config))
            dot_version = calculate(input_string[i+1:], input_config)
            c += hot_spring_version + dot_version
    print(input_string, input_config, c)

    return c

res = 0
factor_1x = []
for i in range(len(springs)):
    visited = set()
    g = calculate(springs[i], configs[i])
    factor_1x.append(g)
    res += g
    # print(i, g, res, "total:", len(ll))
print(res)

