ll = [x for x in open('input.txt').read().strip().split('\n')]

sA, sB = 0, 0
for l in ll:
    A, B = 0, 0
    diff = [inputs := [int(i) for i in l.split()]]
    while any(inputs):
        diff.append(inputs := [b - a for a, b in zip(inputs, inputs[1:])])
    sA += [A := diff[i][-1] + A for i in reversed(range(len(diff) - 1))][-1]
    sB += [B := diff[i][0] - B for i in reversed(range(len(diff) - 1))][-1]

print(sA, sB)