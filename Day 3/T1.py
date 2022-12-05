with open('day 3/input.txt', 'r') as f:
    backpacks = f.read().splitlines() 

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = int()

for backpack in backpacks:
    founditems = []
    length = int(len(backpack) / 2)
    
    #find letters
    for char in backpack[:length]:
        if backpack[length:].find(char) != -1:
            founditems.append(char)
    
    #score found letters
    for item in "".join(set(founditems)):
        score += alphabet.find(item) + 1

print(score)