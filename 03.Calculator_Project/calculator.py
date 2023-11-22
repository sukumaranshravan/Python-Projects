# Calculator
# creating functions to operate
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
# creating a dictionary for oparations
operations={'+':add,'-':subtract,'*':multiply,'/':divide}
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))

for key in operations:
    choose=input(f'Do you want to {key}, enter y/n :')
    if choose=='y':
        calculate=operations[key]
        print(calculate(a,b))
        break
