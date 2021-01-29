#!/usr/bin/env python3
import random
sticks = 21

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will lose")
while True:
    print("Sticks left: " , sticks)
    if sticks == 1:
        if i == 0:
            print("You are win!")
            break
        elif i == 1:
            print("You took the last stick, you lose")
            break
        break
    stick = random.randint(1,4)
    print("Computer took: " , stick)
    i = 1
    sticks_taken = int(input("Take sticks(1-4):"))
    i = 0
    print("\n")
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue

    sticks -= (stick + sticks_taken)
