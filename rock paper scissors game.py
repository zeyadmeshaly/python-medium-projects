import random
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
   player = input("enter rock paper or scissors ")

print(f"Computer chose {computer}")
print(f"Player chose {player}")

if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "scissors":
    print("You lose!")
elif player == "scissors" and computer == "rock":
    print("You lose!")
elif player == "scissors" and computer == "paper":
    print("You win!")
elif player == "rock" and computer == "paper":
    print("You lose!")
elif player == "paper" and computer == "rock":
    print("You win!")

import os
os.system("pause")
