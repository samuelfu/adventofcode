ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

time = int(''.join(ll[0].split(':')[1].split()))
record = int(''.join(ll[1].split(':')[1].split()))
# print(ll)
print(time)
print(record)

ways = 0
for button_pressed in range(1, time + 1):
    distance = (time - button_pressed) * (button_pressed)
    if distance > record:
        ways += 1
        # print("speed", button_pressed, "distance", distance, "ways", ways)
print(ways)
