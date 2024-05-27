# Write a Program to calculate electricity bill (accept number from user).

num = int(input('Enter Your Electricity Bill Units'))

amount = 0

if num<100:
    print("Your Electricity Bill is Free")

elif num>100 and num<=200:
    amount(num-100)*5
    print('Your Electricity Bill is ', amount)

elif num>200:
    amount = 500 + (num-200)*10
    print('Your Electricity Bill is ', amount)

else:
    print("Your Bill is not generated")