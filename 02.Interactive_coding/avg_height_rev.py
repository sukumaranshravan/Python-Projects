# without using len() function

print("Enter the height of each students continously with a space after each entry")
student_heights=input().split()
total_students=0
for student in student_heights:
    total_students+=1
sum=0
for height in student_heights:
    sum=sum+int(height)
average_height=sum/total_students
print(f"total height = {sum}")
print(f"number of students = {total_students}")
print(f"average height = {average_height}")
