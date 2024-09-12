import random

stages = [
"""
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
--------
""",
"""
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
--------
""",
"""
   -----
   |   |
   O   |
  /|\  |
       |
       |
--------
""",
"""
   -----
   |   |
   O   |
  /|   |
       |
       |
--------
""",
"""
   -----
   |   |
   O   |
   |   |
       |
       |
--------
""",
"""
   -----
   |   |
   O   |
       |
       |
       |
--------
""",
"""
   -----
   |   |
       |
       |
       |
       |
--------
"""
]

word_list = ["aardvark","baboon","camel"]
correct_letters = []
random_word = random.choice(word_list)

display = ""
for number in range(len(random_word)):
    display += "_"

print(display)

life_player = len(stages)

while life_player > 0:

    display = ""
    print(display)
    input_choice_letter = input("Guess a letter? ").lower()

    print(input_choice_letter)
    checker = False
    for letter in random_word:
        if letter == input_choice_letter:
            checker = True
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display +="_"

    if not checker:
        life_player -= 1
        print("Your guess is wrong !!!")
    print(stages[life_player])
    print(display)
    print(" ")


    if "_" not in display:
        print("You Won the game")
        life_player = 0
    elif life_player == 0:
        print("You Lose the game")


print(f"The random word is {random_word}")