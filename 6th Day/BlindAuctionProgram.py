from art import logo


bids ={}
auction_start = True

def compute_tally_action():
    winner_name = ""
    winner_bid = 0
    for keys in bids:
        if bids[keys] >= winner_bid:
            winner_name = keys
            winner_bid = bids[keys]

    print(f"The winner is {winner_name} with a bid of ${winner_bid}")




print(logo)


while auction_start:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue.lower() == "no":
        auction_start = False
        compute_tally_action()
    else:
        print("\n" * 20)
