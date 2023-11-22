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
a=int(input("Enter a number :"))
# using while loop for continuing the calculation with the last answer...
flag=True
while flag is True:
    for key in operations:
        print(key)
    operand=input("Choose any of the operations listed above :")
    calculate=operations[operand]
    b=int(input("Enter the another number :"))
    answer=calculate(a,b)
    more=input("Do you want to perform another calculation? y/n")
    if more =='y':
        a=answer
    else:
        print(f"{a}{operand}{b}={answer}")
        print("End of Calculation")
        flag=False
