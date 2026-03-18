print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket fee is $5")
    elif age <= 18:
        print("Your ticket fee is $7")
    else:
        print("Your ticket fee is $10")
else:
    print("Sorry, you need to grow taller before you can ride.")
