print("Welcome to the Roller Coaster Ticket System!\n")

user_height = int(input("What is your height in cm? "))

if user_height >= 120:
    age = int(input("How old are you? "))
    
    if age < 12:
        print("Child ticket price is $5")
        bill = 5
    elif age <= 18:
        print("Teen ticket price is $10")
        bill = 10
    else:
        print("Adult ticket price is $15")
        bill = 15
    
    # Photo option
    photo_req = input("Do you want a photo? Type 'y' for Yes or 'n' for No: ")
    if photo_req.lower() == 'y':
        bill += 3

    print(f"Your total bill is ${bill}")

else:
    print("Sorry, your height is less than 120 cm!")
