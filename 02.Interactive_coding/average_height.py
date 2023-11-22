#using len() function

print("Enter the height of each students continously with a space after each entry")
student_heights=input().split()
total_students=len(student_heights)
sum=0
for height in student_heights:
    sum=sum+int(height)
average_height=sum/total_students
print("total height =",sum)
print("number of students =",total_students)
print("average height =",round(average_height))
