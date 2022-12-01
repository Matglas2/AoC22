#Part 1

with open('input.txt', 'r') as f:
    lines = f.readlines()

count = 0
maxcount = 0

for food in lines:
    if food == '\n':
        if maxcount < count:
            maxcount = count
        count = 0
    else:
        count += int(food[:-1])

print(maxcount)
