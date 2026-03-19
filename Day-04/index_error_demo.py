# Day 04 - IndexError Demonstration

# Flat list of US States
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
    "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
    "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
    "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# ✅ Valid index
print(states_of_america[49])

# ❌ IndexError if uncommented
# print(states_of_america[50])

# ✅ Safe way using len()
num_states = len(states_of_america)
print(states_of_america[num_states - 1])

# -------- Nested Lists --------
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

# Accessing nested list items
print(dirty_dozen)          # whole nested list
print(dirty_dozen[0])       # fruits
print(dirty_dozen[1])       # vegetables
print(dirty_dozen[0][1])    # Nectarines
