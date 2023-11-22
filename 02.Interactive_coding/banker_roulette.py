import random
name_string=input("Enter the names of your group members :")
names=name_string.split(", ")
turn=len(names)
pay=random.randint(0,turn-1)# 1 is deducted as counting starts from 0.
treat=names[pay]
print(treat,"is going to buy the meal today!")
