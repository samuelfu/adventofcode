file_name = 'input.txt'

res = 0

letters = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open(file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        t = line.strip()  # Using strip() to remove newline characters at the end of each line
        t = t.replace("one", "o1e")
        t = t.replace("two", "t2o")
        t = t.replace("three", "th3ee")
        t = t.replace("four", "f4ur")
        t = t.replace("five", "f5ve")
        t = t.replace("six", "s6x")
        t = t.replace("seven", "se7en")
        t = t.replace("eight", "ei8ht")
        t = t.replace("nine", "n9ne")
        print(t)
        t = ''.join(map(lambda x: x if x.isdigit() else '', t))
        print(t)
        s = int(t[0] + t[-1])
        print(s)
        res += s

print(res)
