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

computer = [1, 2, 3]
computer_choice = random.choice(computer)
print(computer_choice)
your_choice = int(
    input("Enter your choice 1/2/3 for Rock/Paper/Scissor respectively. "))
if your_choice == 1 and computer_choice == 1:
    you = rock
    comp = rock
    print(you, "You\n", comp, "Computer\n")
    print("Draw")
elif your_choice == 1 and computer_choice == 2:
    you = rock
    comp = paper
    print(you, "You\n", comp, "Computer\n")
    print("Computer Wins")
elif your_choice == 1 and computer_choice == 3:
    you = rock
    comp = scissors
    print(you, "You\n", comp, "Computer\n")
    print("You Wins")
elif your_choice == 2 and computer_choice == 1:
    you = paper
    comp = rock
    print(you, "You\n", comp, "Computer\n")
    print("You Wins")
elif your_choice == 2 and computer_choice == 2:
    you = paper
    comp = paper
    print(you, "You\n", comp, "Computer\n")
    print("Draw")
elif your_choice == 2 and computer_choice == 3:
    you = paper
    comp = scissors
    print(you, "You\n", comp, "Computer\n")
    print("Computer Wins")
elif your_choice == 3 and computer_choice == 1:
    you = scissors
    comp = rock
    print(you, "You\n", comp, "Computer\n")
    print("Computer Wins")
elif your_choice == 3 and computer_choice == 2:
    you = scissors
    comp = paper
    print(you, "You\n", comp, "Computer\n")
    print("You Wins")
else:
    you = scissors
    comp = scissors
    print(you, "You\n", comp, "Computer\n")
    print("Draw")
