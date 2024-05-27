# Accept the age of 4 People and display the oldest one.

age1 = int(input('Enter Age of First Person'))
age2 = int(input('Enter Age of First Second'))
age3 = int(input('Enter Age of First Third'))
age4 = int(input('Enter Age of First Fourh'))

if age1>age2 and age1>age3 and age1>age4:
    print('Age Of Oldest Person is', age1)

elif age2>age1 and age2>age3 and age2>age4:
    print('Age Of Oldest Person is', age2)

elif age3>age1 and age3>age2 and age3>age4:
    print('Age Of oldest Person is', age3)

elif age4>age1 and age4>age2 and age4>age3:
    print('Age Of oldest Person is', age4)

elif age1 or age2 or age3 or age4 == 0:
    print("Entered Wrong Age")