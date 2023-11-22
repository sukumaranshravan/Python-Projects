import random
toss = input("Type H for Heads or T for Tails as per your wish !!")
if toss == 'h' or toss == 't':
  result = random.randint(0, 1)
  if result == 0:
    print("Tails")
  else:
    print("Heads")
else:
  print("Wrong Entry!!, Please Try again.")
