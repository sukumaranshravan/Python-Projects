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
next='yes'
while next=='yes':
    name=input('enter your name :')
    bid=int(input('enter the amount :'))
    bids[name]=bid
    next=input("Any other Bidder? type 'yes' or 'no' ")
    if 'yes':
        clean()

bid_list=[]
name_list=[]

for k in bids:
    bid_list.append(bids[k])
    name_list.append(k)
highest_bid=max(bid_list)
index_bid=bid_list.index(highest_bid)
winner=name_list[index_bid]
print(f"The winner is {winner} with highest bid of {highest_bid}")
