import re

with open('day 5/input.txt', 'r') as f:
    inputdata = f.read().splitlines()

blockinput = []

# get all block lines on the input in a file and count highest stack in the process
i = 0
while not inputdata[i].startswith(" 1"):
    blockinput.append(inputdata[i])
    i += 1

# determine the amount of stacks in the input by counting the stack id's
stackids = re.findall("(\d+)", inputdata[i])

# prepare a array with the same anout of subarrays (all empty)
stacks =  [[] for x in range(len(stackids))]

for blockline in blockinput:
    # regex my way out of interpreting the input blocks
    blocks = re.findall("(\w|\s{4})", blockline)
    
    # put block in order in to the precreatred arrays
    stackid = 0
    for block in blocks:
        if block != "    ":
            stacks[stackid].append(block)
        stackid += 1

for actionline in inputdata[i +2:]:
    # parse the actions
    action = re.findall("\d+",actionline)

    # move block to front of array
    for x in range(int(action[0])):
        block = stacks[int(action[1]) -1].pop(0)
        #reverse order
        #stacks[int(action[2]) -1].insert(0, block)
        #same order
        stacks[int(action[2]) -1].insert(0 + x, block)

# find answer
answer = ""
for stack in stacks:
    answer += (stack[0])

print(answer)