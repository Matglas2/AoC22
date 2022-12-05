with open('day 3/input.txt', 'r') as f:
    backpacks = f.read().splitlines() 

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = int()
groupsize = 3

backpackgroups = []

#group in sets of 3
for index in range(0, len(backpacks), groupsize):
    backpackgroups.append(backpacks[index:index+groupsize])

#find and score letters. needs to care about groupsize in the future
for backpackgroup in backpackgroups:
    founditems = []

    #Find common letters in group 1 and 2
    for char in backpackgroup[0]:
        if backpackgroup[1].find(char) != -1:
            founditems.append(char)
    
    #use distinct list to find last match and cancel as soon as its found
    for char in "".join(set(founditems)):
        if backpackgroup[2].find(char) != -1:
            score += alphabet.find(char) + 1
            continue

print(score)