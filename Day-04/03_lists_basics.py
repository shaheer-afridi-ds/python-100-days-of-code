# List Data Structure Example

# List of US States
states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
    "Virginia", "New York", "North Carolina", "Rhode Island",
    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
    "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
    "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
    "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
    "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
    "North Dakota", "South Dakota", "Montana", "Washington",
    "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
    "Arizona", "Alaska", "Hawaii"
]

# Indexing starts from 0
# Example: index 1 will access "Pennsylvania"
print(states_of_america[1])
states_of_america[1] = "Pencilvania"  # modifying element

# Adding one item
states_of_america.append("Shaheerland")

# Adding multiple items
states_of_america.extend(["Shaheerland", "Jack Bauer Land"])

# Print final list
print(states_of_america)
