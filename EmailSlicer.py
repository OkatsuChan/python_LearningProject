

email = input("Enter your email: ")

# Bro123@gmail.com



username = email[:email.index("@")]
domain =  email[email.index("@")+1:]

print(f"username is {username} and doimaind is {domain}")