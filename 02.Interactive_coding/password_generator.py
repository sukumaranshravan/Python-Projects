#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass_letter=list()
for i in range(0,nr_letters):
    letter=letters[random.randint(0,51)]
    pass_letter.append(letter)
pass_symbol=list()
for i in range(0,nr_symbols):
    symbol=symbols[random.randint(0,8)]
    pass_symbol.append(symbol)
pass_number=list()
for i in range(0,nr_numbers):
    number=numbers[random.randint(0,9)]
    pass_number.append(number)
password=[pass_letter,pass_symbol,pass_number]
for i in pass_letter:
    print(i,end='')
for j in pass_symbol:
    print(j,end='')
for k in pass_number:
    print(k,end='')
print('\n')
