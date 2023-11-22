logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def clean():
    import os
    clear = lambda: os.system('clear')
    clear()
bids={}
def highest_bid(bids):
    highest_amount=0
    winner=""
    for key in bids:
        bid_amount=bids[key]
        if bid_amount>highest_amount:
            highest_amount=bid_amount
            winner=key
    print(f"The winner is {winner} with highest bid of {highest_amount}")

next='yes'
while next=='yes':
    name=input('enter your name :')
    bid=int(input('enter the amount :'))
    bids[name]=bid
    next=input("Any other Bidder? type 'yes' or 'no' ")
    if next=='yes':
        clean()
    else:
        highest_bid(bids)
