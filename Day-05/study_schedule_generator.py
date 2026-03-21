import random
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Computer Science']
time_blocks = ['30 min', '45 min', '60 min', '90 min']
breaks = ['5 min', '10 min', '15 min', '20 min']

nr_subjects = int(input("how many subjects do u want to study?\n"))
nr_time_blocks = int(input("how much times do u want to study?\n"))
nr_breaks = int(input("how much  breaks do u want in mid study?\n"))

time_table_list = []
for char in range(0, nr_subjects):
    time_table_list.append(random.choice(subjects))

for char in range(0, nr_breaks):
    time_table_list.append(random.choice(breaks))

for char in range(0, nr_time_blocks):
    time_table_list.append(random.choice(time_blocks))

for item in time_table_list:
    print(item)
