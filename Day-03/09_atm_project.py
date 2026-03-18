print("Welcome to the Python ATM!\n")

balance = 1000

user_input = input(
    "What would you like to do?\n"
    "Press 1 to Check Balance\n"
    "Press 2 to Deposit Money\n"
    "Press 3 to Withdraw Money\n"
)

if user_input == "1":
    print(f"Your current balance is: ${balance}")
elif user_input == "2":
    deposit = int(input("How much would you like to deposit?\n"))
    balance += deposit
    print(f"${deposit} successfully deposited. New balance: ${balance}")
elif user_input == "3":
    withdraw = int(input("How much would you like to withdraw?\n"))
    if withdraw <= balance:
        balance -= withdraw
        print(f"${withdraw} successfully withdrawn. New balance: ${balance}")
    else:
        print("Insufficient funds!")
else:
    print("Invalid selection. Please try again.")
