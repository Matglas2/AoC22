with open('day 7/input.txt', 'r') as f:
    inputdata = f.read().splitlines()

inputdata.reverse()
foldersizes = {}

i = int()
answer = int()
foldersize = 0
seen = []

# find size of root and save all seen folder sizes
while i < len(inputdata):
    line = inputdata[i].split()
    if line[0].isnumeric(): 
        foldersize += int(line[0])
    elif line[0] == 'dir':
        foldersize += foldersizes[line[1]]
    elif line[1] == 'ls':
        foldersizes[inputdata[i +1][5:]] = foldersize
        seen.append(foldersize)
        foldersize = 0
    i += 1

target = foldersizes["/"] - 40000000

best = foldersizes["/"]
for size in seen:
    if size < best and size > target:
        best = size

seen.sort()

print(seen)
print(foldersizes["/"])
print(target)

# :(