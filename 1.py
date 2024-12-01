from collections import Counter

# part 1
ll = [x for x in open('1.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

each_line = [p.split() for p in ll]
first_list, second_list = zip(*each_line)

sorted_first_list = sorted(first_list)
sorted_second_list = sorted(second_list)

sum = 0
for i in range(len(sorted_first_list)):
    sum += abs(int(sorted_first_list[i]) - int(sorted_second_list[i]))

print(sum)

# part 2
sum = 0
counter_of_list_2 = Counter(second_list)
for i in range(len(first_list)):
    sum += counter_of_list_2[first_list[i]] * int(first_list[i])

print(sum)
