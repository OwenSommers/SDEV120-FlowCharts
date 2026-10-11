# Program: Identify Even and Odd Numbers
# Description: Creates a list of 15 numbers and determines
#              whether each number is even or odd.

# Declare a list containing 15 numbers
numbera = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Loop through each number in the list
for number in numbera:

    # Determine whether the number is even
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
