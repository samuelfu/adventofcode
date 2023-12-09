import math

def get_steps(starting_node):
    steps = 0
    i = 0
    while starting_node[-1] != 'Z':
        starting_node = m[starting_node][0] if instructions[i] == 'L' else m[starting_node][1]
        steps += 1
        i += 1
        if i == len(instructions):
            i = 0

    return steps

print([m:={},
       ll:=[x for x in open('input.txt').read().strip().split('\n')],
       instructions:=ll[0],
       math.lcm(*[get_steps(n) for n in [node[0] for node in [(coords[:3], m.update({coords[:3]:(coords[7:10],coords[12:-1])}))
                                                              for coords in ll[2:]] if node[0][-1] == 'A']])
       ][-1])
