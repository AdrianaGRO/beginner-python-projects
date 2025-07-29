"""
Project: Secret Auction
Description: Create a dictionary mapping bidder names to their bid amounts. Implement a function to determine the highest bidder.

# TODO-1: Create a dictionary with bidder names as keys and bid amounts as values.
# TODO-2: Define a function that takes the bids dictionary as an argument.
# TODO-3: In the function, find the highest bid and corresponding bidder.
# TODO-4: Return a formatted string with the winner's name and bid amount.

Output Format:
The winner is Alice with a bid of $200.

Sample Call:
get_highest_bidder({"Alice": 200, "Bob": 150})
# Expected: The winner is Alice with a bid of $200.

Note: Use hard-coded values for testing, not input().
"""

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

