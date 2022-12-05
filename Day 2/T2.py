# A = Rock
# B = Paper
# C = Scissors

# X = 1 = Rock = lose
# Y = 2 = Paper = tie
# Z = 3 = Scissors = win

# lose = 0
# tie = 3
# win = 6

# AX = 4 = lose = AZ = 3
# AY = 8 = tie = AX = 4
# AZ = 3 = win = AY = 8
# BX = 1 = lose = BX = 1
# BY = 5 = tie = BY = 5
# BZ = 9 = win = BZ = 9
# CX = 7 = lose = CY = 2
# CY = 2 = tie = CZ = 6
# CZ = 6 = win = CX = 7

with open('day 2/input.txt', 'r') as f:
    games = f.read().splitlines() 

score = int()
for game in games:
    match game:
        case "A X":
            score += 3
        case "A Y":
            score += 4
        case "A Z":
            score += 8
        case "B X":
            score += 1
        case "B Y":
            score += 5
        case "B Z":
            score += 9
        case "C X":
            score += 2
        case "C Y":
            score += 6
        case "C Z":
            score += 7                                                                       
        case _:
            score += 0

print(score)