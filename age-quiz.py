""" This is an if-elif-else statement that prints out different 
messages according to the user's age. """

# int() function casts users age input, from string to an integer.

age = int(input("Please enter your age: "))

# Arrange if-elif statements in descending order regarding age.
# If the condition, 'age >= 40', was put as the starting if statement, 
# the flow of logic would overide the next elif statements 
# >= 65 and > 100 and their respective messages would not be output.

# This is because the conditional, 'age >=40', covers all numbers over 40,
# so the flow of logic would output the first conditional 
# and not need to output the next two.

if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")

"""This is an alternative code 
with an if statement nested within another if statement"""

while True:
    age = int(input("Please enter your age or '-1' to exit: "))
    if age >= 40:
        if age >= 65 and age <= 100 :
            print("Enjoy your retirement!")
        elif age > 100:
            print("Sorry, you're dead.")
        else:
            print("You're over the hill.")
    elif age < 13 and age != -1:
        print("You qualify for the kiddie discount.")
    elif age == 21:
        print("Congrats on your 21st!")
    elif age == -1:
        print("Thank you for using the age quiz.")
        break
    else:
        print("Age is but a number.")
