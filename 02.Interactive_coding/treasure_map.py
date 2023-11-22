line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if position=='a1':
  map[0][0]='x'
elif position=='b1':
  map[0][1]='x'
elif position=='c1':
  map[0][2]='x'
elif position=='a2':
  map[1][0]='x'
elif position=='b2':
  map[1][1]='x'
elif position=='c2':
  map[1][2]='x'
elif position=='a3':
  map[2][0]='x'
elif position=='b3':
  map[2][1]='x'
else:
  map[2][2]='x'    
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")