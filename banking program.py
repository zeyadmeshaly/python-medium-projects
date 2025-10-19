def show_balane():
    print("-----BANK ACCOUNT-----")
    print(f"your balance is EG{balance:.2f} ")

def deposit():
    amount = float(input("enter amount to deposit: "))

    if amount < 0:
        print("amount cannot be negative")
        return 0
    else:
        return amount

def withdraw():
    withdrawn = float(input("enter amount to withdraw: "))

    if withdrawn > balance:
        print("you don't have enough money")
        return 0
    else:
        return withdrawn

balance = 0
is_running = True

while is_running:
    print("banking program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("enter your choice "))

    match choice:
        case 1:
            show_balane()
        case 2:
            balance += deposit()
        case 3:
            balance -= withdraw()
        case 4:
            is_running = False
        case _:
            print("invalid choice")

print("thank you! have a nice day!")

import os
os.system("pause")