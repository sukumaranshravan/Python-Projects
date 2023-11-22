# if divide by 3 then fizz, if divided by 5 then buzz, if divided by both 3 and 5 fizzbuzz
# this program is to print fizz buzz as per the above condition from 1 to 100
for number in range(1,101):
    if number%3==0 and number%5==0:
        print('fizzbuzz')
    elif number%3==0:
        print('fizz')
    elif number%5==0:
        print('buzz')
    else:
        print(number)
