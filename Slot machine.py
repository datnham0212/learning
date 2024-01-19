#Slot Machine
import random as r 
from itertools import groupby

# Borrowed from Stack Overflow. Use for Jackpot
def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def within_range(n):
    check = 0
    confirm = False
    for i in range(3):
        if n[i] in range(0,5):
            check += 1
    if check == 3:
        confirm = True
    return confirm


coin = int(input("Insert coins: ")) # 2 coins per spin
print(coin) 

spin = int(coin/2)

for j in range(spin):
    n = []
    for i in range(3): # Standard slot machines need 3 reels minimum 
        i = r.randint(0,5) # Like typical slot machines, it needs 6 different symbols
        n.append(i)
    print("Jackpot!") if all_equal(n) == True and within_range(n) else print("Try again!")
    print(n)
    n.clear()

# 16/1/2024: This is just a basic idea of a slot machine. More to come...
# 17/1/2024: Added coin insert
# 18/1/2024: Just making sure that the numbers in randint is within range
# 19/1/2024: 