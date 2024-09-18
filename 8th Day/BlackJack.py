import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_score(c_score,p_score):
    if p_score == c_score:
        print("Draw 🙃")
    elif p_score > 21:
        print("You went over. You lose 😭")
    elif c_score > 21:
        print("Opponent went over. You win 😁")
    elif c_score > p_score:
        print("You win 😃")


def card_random_picker():
    return random.choice(cards)

def checker_blackjack(list_card):
    if 11 in list_card and 10 in list_card:
        return True
    return False

def compute_list_cards(list_card):

    if 11 in list_card and sum(list_card) > 21:
        list_card.remove(11)
        list_card.append(1)

    return sum(list_card)


def play_game():
    computer_score = 0
    player_score = 0
    player_one_cards = []
    computer_cards = []
    for index in range(2):
        player_one_cards.append(card_random_picker())
        computer_cards.append(card_random_picker())

    play = True
    while play :
        computer_score = compute_list_cards(computer_cards)
        player_score = compute_list_cards(player_one_cards)
        print(f"Your cards: {player_one_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if checker_blackjack([player_one_cards]) and not checker_blackjack(computer_cards):
            print("Player Wins")
        elif checker_blackjack(computer_cards):
            print("Computer Wins")
        else:
            if player_score > 21:
                play = False
            else:
                user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_deal == "y":
                    player_one_cards.append(card_random_picker())
                elif user_deal == "n":
                    play = False

    while computer_score < 16:
        computer_cards.append(card_random_picker())
        computer_score = compute_list_cards(computer_cards)

    print(f"Your final hand: {player_one_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    check_score(computer_score,player_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print(logo)
    play_game()
    print("\n" * 2)
