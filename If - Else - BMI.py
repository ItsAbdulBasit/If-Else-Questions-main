# The BMI is calculated by dividing a person’s weight (in kg) by the square of their height (in m) .
# Take height and weight from the user.
weight = float(input("Enter your weight in kilograms: "))

height = float(input("Enter your height in meters: "))

bmi = weight/ (height** 2)

if bmi < 18.5:
    print('You are underweight.')
elif 18.5 <= bmi < 25: 
    print('You have a normal weight.')
elif 25 <= bmi < 30:
    print('You are slightly overweight.')
elif 30 <= bmi < 35:
    print('You are obese.')
else:
    print('You are clinically obese.')

    