import random

low = 1
high = 100
chances = 3

answer = random.randint(low, high)

while chances > 0:
    guess = int(input(f"enter a number between {low} and {high}: "))

    if guess == answer:
        print(f"you guessed right!")
        print("----YOU WIN! !----")
        break
    else:
        chances -= 1
        if chances >0:
            print(f"you guessed wrong. {chances} chances left")
        else:
            print("----GAME OVER---- YOU LOSE !")
            print(f"{answer} was the right answer")

import os
os.system('pause')
