print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line
name=name1+name2
letters=len(name)
true_counter=0
love_counter=0
t=['t','r','u','e']
l=['l','o','v','e']

for i in name[0:letters]:
    if i in t:
        true_counter+=1
for j in name[0:letters]:
    if j in l:
        love_counter+=1

score=int(str(true_counter)+str(love_counter))

if score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >40 and score <50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")
