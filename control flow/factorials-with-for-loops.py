# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here

number = 6

factorial = 1

if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial*i
    print("The factorial of", number, "is", factorial)

# print the factorial of number
