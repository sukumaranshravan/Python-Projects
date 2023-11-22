# here for and if loops are used to find maximum score among a list of scores instead of max() function in python3
score=input().split()
print(score)
high_score=0
for i in score:
    current_score=int(i)
    if current_score>high_score:
        high_score=current_score
print(high_score)
