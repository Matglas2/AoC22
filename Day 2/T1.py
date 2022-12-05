# A = Rock
# B = Paper
# C = Scissors

# X = 1 = Rock = lose
# Y = 2 = Paper = tie
# Z = 3 = Scissors = win

# lose = 0
# tie = 3
# win = 6

# AX = 4
# AY = 8 
# AZ = 3
# BX = 1
# BY = 5
# BZ = 9
# CX = 7 
# CY = 2
# CZ = 6

with open('day 2/input.txt', 'r') as f:
    games = f.read().splitlines() 

score = int()
for game in games:
    match game:
        case "A X":
            score += 4
        case "A Y":
            score += 8
        case "A Z":
            score += 3
        case "B X":
            score += 1
        case "B Y":
            score += 5
        case "B Z":
            score += 9
        case "C X":
            score += 7
        case "C Y":
            score += 2
        case "C Z":
            score += 6                                                                        
        case _:
            score += 0

print(score)