with open('day 3/input.txt', 'r') as f:
    backpacks = f.read().splitlines() 

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = int()
groupsize = 3

backpackgroups = []

for index in range(0, len(backpacks), groupsize):
    backpackgroups.append(backpacks[index:index+groupsize])

for backpackgroup in backpackgroups:
    founditems = []

    #find and score letters. needs to care about groupsize in the future
    for char in backpackgroup[0]:
        if backpackgroup[1].find(char) != -1:
            founditems.append(char)
    
    for char in "".join(set(founditems)):
        if backpackgroup[2].find(char) != -1:
            score += alphabet.find(char) + 1
            continue

print(score)