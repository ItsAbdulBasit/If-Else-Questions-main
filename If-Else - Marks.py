# Write a program to accept percentage from user and display the grade.

per = int(input('Enter Your Grade\n'))

if per>90:
    print("Grade is A")

elif per>80 and per<=90:
    print('Grade is B')

elif per>=60 and per<=80:
    print('Grade C')

elif per == 60:
    print("Grade is D")

else:
    print('Failed')

