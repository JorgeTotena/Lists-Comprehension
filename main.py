"""List comprehension are a way of creating new lists from a for loop without needing to create an iteration
Example:
    numbers = [1, 2, 3]
    new_list = []
    for n in numbers:
        add_1 = n + 1
        new_list.append(add_1)

with list comprehension:
new_list = [new_item for item in list]
name = Angela
new_list = [letter for letter in name]

applying the logic, the new list comprehension would look like this
new_list = [n+1 for n in numbers]

"""

"""Challenge Create a new list from a range, where the list items are double in the range
doubled = []

for i in range(1,5):
    number_doubled = i * 2
    doubled.append(number_doubled)

print(doubled)
"""

#Conditional Lists Comprehension
"""We can also add conditions to the list comprehension, the formula would look something like this
new_list = [new_item for item in list if test]
"""
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
#CHALLENGE - ADD A LIST OF ALL THE NAMES WITH 5 OR MORE CHARACTERS AND MAKE THEM UPPERCASE
#With lists comprehensions
upper_names = [name.upper() for name in names if len(name) >= 5]
new_doubled = [number_doubled * 2 for number_doubled in range(1,5)]
print(upper_names)

#Nested lists comprehensions
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)
