
#Part 2

with open('input.txt', 'r') as f:
    lines = f.readlines()

count = int()
elves = []

for food in lines:
    if food == '\n':
        elves.append(count)
        count = 0
    else:
        count += int(food[:-1])

elves.sort(reverse = True)

print(elves[0], elves[1], elves[2])
print(elves[0] + elves[1] + elves[2])
