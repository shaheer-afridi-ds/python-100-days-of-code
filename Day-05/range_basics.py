# range() example
print(range(1, 10))  # Doesn't print numbers directly

# Loop from 1 to 9
for number in range(1, 10):
    print(number)

# Loop from 1 to 10
for number in range(1, 11):
    print(number)

# Gauss Challenge (sum from 1 to 100)
total = 0
for number in range(1, 101):
    total += number

print("Total:", total)
