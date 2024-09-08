import random

rock= '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

paper= '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

scissors= '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
choice = [rock, paper, scissors]
user_choice = int(input("Enter your choice (0 for rock, 1 for paper, 2 for scissors): "))

bot_choice = random.randint(0,2)

print(choice[user_choice])
print("Computer Chose")
print(choice[bot_choice])

if user_choice == bot_choice:
    print("It's a tie!")
elif user_choice == 0 and bot_choice == 2 or user_choice == 1 and bot_choice == 0 or user_choice == 2 and bot_choice == 1:
    print("You win!")
else:
    print("You lose!")




# choice = ["rock", "paper", "scissors"]
#
# user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#
# while user_choice not in choice:
#     user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
#
# bot_choice = random.choice(choice)
#
# if user_choice == "rock":
#     print(rock)
# elif user_choice == "paper":
#     print(paper)
# elif user_choice == "scissors":
#     print(scissors)
#
# print("Computer Chose")
# if bot_choice == "rock":
#     print(rock)
# elif bot_choice == "paper":
#     print(paper)
# elif bot_choice == "scissors":
#     print(scissors)
#
#
#
# if user_choice == bot_choice:
#     print("It's a tie!")
# elif user_choice == "rock" and bot_choice == "scissors" or user_choice == "scissors" and bot_choice == "paper" or user_choice == "paper" and bot_choice == "rock":
#     print("You win!")
# else:
#     print("You lose!")

