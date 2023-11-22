import random
from hangman_art import stages
from hangman_words import word_list
chosen_word=random.choice(word_list) # random.choices means, it will chose cat or bat altogether this will cause line 6 of program to print only 1 item in the display list.
print(f"hey word randomly chosen is {chosen_word}")
display=[]
for letter in chosen_word: #displaying blanks in the display list which is to be filled with each true guess by the user in the respective position
    display+='_'
count=0
life=6
game_over=False
while game_over is False:
    guess=input("Guess a letter ?: ")
    for i in chosen_word: #this loop will place the user guess in the correct position using list of index, starting from 0th index, count is used for correct indexing
        if i==guess:
            display[count]=i
            count+=1
        else:
            count+=1
    if guess not in chosen_word:
        life-=1
        print(stages[life])
        if life==0:
            print("Game Over You are Hanged.")
            game_over=True
    print(display)
    count=0  # count has to be set to zero after exiting the above loop as count is used for indexing of the guessed letter in the display list, if count not set to 0, means index error will be shown as traceback.
    blanks=display.count("_")
    print(blanks)
    print(life)
    if blanks==0:
        game_over=True
        print("Hurray!! You won the game")
