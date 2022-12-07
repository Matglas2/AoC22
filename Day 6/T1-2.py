with open('day 6/input.txt', 'r') as f:
    inputdata = f.readline().removesuffix('\n')

scansize = 14 # use 4 for part 1
answer = int()

for i in range(len(inputdata) -scansize):
    if len(set(inputdata[i: i+scansize])) == scansize:
        answer = i + scansize
        break

print(answer)