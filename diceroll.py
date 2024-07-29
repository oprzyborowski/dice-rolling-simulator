import random

def checker_n_dice_input(picked_n):
    if picked_n in range(1, 11):
        return picked_n
    else:
        print("Pick a number from 1 to 10.")
        return None

def roll_dices(n_dice):
    roll_result = []
    for _ in range(n_dice):
        each_roll = random.randint(1, 6)
        roll_result.append(each_roll)
    return roll_result

while True:
    try:
        n_dice = int(input("How many dices would you like to throw? [1-10] --> "))
        n_dice = checker_n_dice_input(n_dice)
        if n_dice is not None:
            break
    except ValueError:
        print("Invalid input. Please pick a number from 1 to 10.")
 
roll_result = roll_dices(n_dice)
if n_dice == 1:
    print(f"You threw {n_dice} dice and the result is {roll_result}")
else:
    print(f"You threw {n_dice} dices and the result is {roll_result}")

