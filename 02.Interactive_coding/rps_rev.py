rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
pic=[rock,paper,scissors]
you_choose=int(input("0/1/2 for Rock/Paper/Scissors \n"))
computer_choose=random.randint(0,2)
if you_choose>2:
    print("Wrong Choice, You Lose")
else:
    if you_choose==computer_choose:
        print("You:\n",pic[you_choose],"\ncomputer:\n",pic[computer_choose])
        print("Its a Draw")
    elif you_choose>computer_choose:
        if computer_choose!=0:
            print("You:\n",pic[you_choose],"\ncomputer:\n",pic[computer_choose])
            print("You Wins")
        else:
            print("You:\n",pic[you_choose],"\ncomputer:\n",pic[computer_choose])
            print("You Lose")
    elif computer_choose>you_choose:
        if you_choose!=0:
            print("You:\n",pic[you_choose],"\ncomputer:\n",pic[computer_choose])
            print("You Lose")
        else:
            print("You:\n",pic[you_choose],"\ncomputer:\n",pic[computer_choose])
            print("You Wins")
