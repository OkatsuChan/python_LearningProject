#
#
# name = input("Enter your full name: ")
# phone = input("Enter your phone #: ")
#
# # result =len(name)
# # result  = name.find("o")
# #result  = name.rfind("s") # last occur of the letter we want to find
# # result  = name.capitalize()
# # result  = name.upper()
# # result  = name.lower()
# result  = name.isdigit()
# # result  = name.isalpha()
# # result  = phone.count("-")
# result  = phone.replace("-"," ")
#
#
#
# print(result)


username = input("Enter your username: ")

length = len(username) +1
if length < 12:
    if username.find(" ") == -1:
        if username.isalpha():
            print("Successful Login")
        else:
            print("Dont add number on username")
    else:
        print("Dont put some space on username")
else:
    print("More than 12 character")