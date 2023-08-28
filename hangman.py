import random

STAGES = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
    +---+
    O   |
    |   |
        |
       ===""",
    """
    +---+
    O   |
   /|   |
        |
       ===""",
    """
    +---+
    O   |
   /|\  |
        |
       ===""",
    """
    +---+
    O   |
   /|\  |
   /    |
       ===""",
    """
    +---+
    O   |
   /|\  |
   / \  |
       ===""",
]


fruits = ["mango", "apple", "banana", "orange", "grape"]

fruit = random.choice(fruits)


guess = []
chance = 6

for _ in range(len(fruit)):
    guess += "_"

game_over = False

while not game_over:
    guessed_letter = input("Guess a letter ").lower()
    for position in range(len(fruit)):
        letter = fruit[position]
        if letter == guessed_letter:
            guess[position] = guessed_letter
    print(guess)

    if guessed_letter not in fruit:
        chance -= 1
        if chance == 0:
            game_over = True
            print("You Lose!")

    if "_" not in guess:
        game_over = True
        print("You Win")
    print(STAGES[::-1][chance])
