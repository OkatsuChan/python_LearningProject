import random

from art import logo

life = 0
game_over = False

def random_number():
    return random.choice(range(101))

def check_validity_guess(life):

    if guess > guess_num:
        print("Too high.")
        life -= 1
    elif guess < guess_num:
        print("Too low.")
        life -= 1
    elif guess == guess_num:
        print(f"You got it! The answer was {guess_num}.")
        life = -1
    return life


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
settings = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if settings == "easy":
    life = 10
elif settings == "hard":
    life =5


guess_num = random_number()
print(guess_num)
while not game_over:
    print(f"You have {life} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    life = check_validity_guess(life)
    if life == 0:
        game_over = True
        print("You've run out of guesses, you lose.")
    elif life < 0:
        game_over = True


