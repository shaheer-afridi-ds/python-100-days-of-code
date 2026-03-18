print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    
    # Ticket pricing with logical operator
    if age < 12:
        bill = 5
        print("Child ticket: $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket: $7")
    elif 45 <= age <= 55:
        bill = 0
        print("Free ticket for midlife crises! 🎉")
    else:
        bill = 12
        print("Adult ticket: $12")
    
    # Photo option
    wants_photo = input("Do you want a photo taken? Y or N: ").upper()
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you need to grow taller before you can ride.")
