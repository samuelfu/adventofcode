ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

times = int(''.join(ll[0].split(':')[1].split()))
records = int(''.join(ll[1].split(':')[1].split()))
# print(ll)
print(times)
print(records)

res = 1
for i in range(len(times)):
    record = records[i]
    time = times[i]
    ways = 0
    for button_pressed in range(1, time + 1):
        distance = (time - button_pressed) * (button_pressed)
        if distance > record:
            print("game", i, "speed", button_pressed, "distance", distance)
            ways += 1
    print(ways)
    res *= ways

print(res)