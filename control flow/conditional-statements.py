# Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.

# use this input to make your submission

points = 174 

if points <= 50:
    print("Congratulations! You won a wooden rabbit!")
elif points <= 150:
    print("Congratulations! You won a no prize!")
elif points <= 180:
    print("Congratulations! You won a wafer-thin mint!")
else:
    print("Congratulations! You won a penguin!")
