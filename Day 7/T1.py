with open('day 7/input.txt', 'r') as f:
    inputdata = f.read().splitlines()

inputdata.reverse()
foldersizes = {}

i = int()
answer = int()
foldersize = 0

while i < len(inputdata):
    line = inputdata[i].split()
    if line[0].isnumeric(): 
        foldersize += int(line[0])
    elif line[0] == 'dir':
        foldersize += foldersizes[line[1]]
    elif line[1] == 'ls':
        if foldersize <= 100000: answer += foldersize
        foldersizes[inputdata[i +1][5:]] = foldersize
        foldersize = 0
    i += 1

print(answer)