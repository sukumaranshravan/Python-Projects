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
# operations={'+':add,'-':subtract,'*':multiply,'/':divide}
# a=int(input("Enter a number :"))
# # using while loop for continuing the calculation with the last answer...
# flag=True
# while flag is True:
#     for key in operations:
#         print(key)
#     operand=input("Choose any of the operations listed above :")
#     calculate=operations[operand]
#     b=int(input("Enter the another number :"))
#     answer=calculate(a,b)
#     more=input("Do you want to perform another calculation? y/n")
#     if more =='y':
#         a=answer
#     else:
#         print(f"{a}{operand}{b}={answer}")
#         print("End of Calculation")
#         flag=False
# what if we need to start a new calculation rather than ending it saying 'n' and starting all over?  it can be done using recursion
# recursion is a function calling itself ... this recursion function doesn't take any argument nor it has any parameters.
def calculator():
    operations={'+':add,'-':subtract,'*':multiply,'/':divide}
    a=int(input("Enter a number :"))
    flag=True
    while flag is True:
        for key in operations:
            print(key)
        operand=input("Choose any of the operations listed above :")
        calculate=operations[operand]
        b=int(input("Enter the another number :"))
        answer=calculate(a,b)
        print(f"{a}{operand}{b}={answer}")
        more=input("Do you want to perform another calculation? 'y' to continue with this value, 'n' to start a new calculation or press any other key to quit.")
        if more =='y':
            a=answer
        elif more=='n':
            calculator()
        else:
            print("End of Calculation")
            flag=False
        break
calculator()
