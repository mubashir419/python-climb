import random
print("Welcome to the dice rolling simulator")
while True:
    print("Press enter to roll the dice")
    input()
    number=random.randint(1,6)
    print("You rolled a",number)
    print("Do you want to roll again? (y/n)")
    answer=input()
    if answer=="n":
        break
    else:
        continue
