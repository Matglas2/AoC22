import re

with open('day 4/input.txt', 'r') as f:
    sectorlines = f.read().splitlines() 

count = int()

for line in sectorlines:
    #make array of numbers from string
    s = re.split("[-,]", line)

    #fill in the missing numbers
    r1 = set(range(int(s[0]),int(s[1]) + 1))
    r2 = set(range(int(s[2]),int(s[3]) + 1))
    
    #count any overlap
    if not r1.isdisjoint(r2): count += 1

print(count)