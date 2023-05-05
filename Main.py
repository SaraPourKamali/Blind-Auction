import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")

other_user = True
bidders = {}


def find_highest_bid(bidders_record):
    highest_price = 0
    for bidder in bidders_record:
        bidder_price = bidders_record[bidder]
        if bidder_price > highest_price:
            highest_price = bidder_price
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_price}.")


while other_user:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    other_user = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    os.system("cls")

    bidders[name] = bid

    # print(bidders)
    if other_user == "no":
        other_user = False
        find_highest_bid(bidders)
