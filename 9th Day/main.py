enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)


# Global scope

player_health = 10

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)

drink_potion()


#Block Scope

game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Constants

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

