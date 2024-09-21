def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing? looping until it goes on 20 then print "You got it" if find reach
# 2. When is the function meant to print "You got it"? when find 20
# 3. What are your assumptions about the value of i? nothing need to fix range (1,21)


from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])


year = int(input("What's your year of birth?"))


if year > 1994:
    print("You are a Gen Z.")
elif year > 1980:
    print("You are a millennial.")

try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid input type try numerical number!!!")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You under age {age} to drive.")


pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


import random

def add(n1, n2):
    return n1 + n2

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

