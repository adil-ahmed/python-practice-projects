import random

while True:
    response = input("Roll the dice? (y/n): ").lower()
    print(response)
    if response == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')
    elif response == 'n':
        print("No problem! Thanks for playing. Have a good day.")
        break
    else:
        print("Invalid choice!")

