file_name = 'input.txt'

res = 0
all_colors = ["red", "green", "blue"]
input_colors = [12, 13, 14]
l = 1

cube = 0
with open(file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        t = line.strip()  # Using strip() to remove newline characters at the end of each line
        t = t[t.find(':')+2:]
        games = t.split(";")
        game_valid = True
        print("Line " + str(l) + " Games: " + str(games))
        max_green = 0
        max_red = 0
        max_blue = 0

        for g in games:
            green = 0
            red = 0
            blue = 0

            colors = g.split(",")
            for color in colors:
                c = color.strip()
                c = c.split(" ")
                if c[1] == "green":
                    green += int(c[0])
                    max_green = max(max_green, green)
                elif c[1] == "red":
                    red += int(c[0])
                    max_red = max(max_red, red)
                else:
                    blue += int(c[0])
                    max_blue = max(max_blue, blue)
            if green <= input_colors[1] and red <= input_colors[0] and blue <= input_colors[2]:
                continue
            else:
                game_valid = False

        if game_valid:
            res += l
        print(max_green, max_red, max_blue)
        cube += max_green * max_red * max_blue

        l += 1

print(res)
print(cube)
