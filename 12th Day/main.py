

class User:

    def __init__(self,id,username):
        self.id =id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    pass

user_1 = User(1001,"Tian")
user_2 = User(111,"jean")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# print(user_1.id,user_1.username),
# print(user_1.followers)
#
# # user_2 = User() ou can use constructor for intialize or this
# # user_2.id = 01
# # user_2.name = "baby"
