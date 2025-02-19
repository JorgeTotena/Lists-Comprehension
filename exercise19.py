# Open 'file1.txt' in read mode and assign the file object to 'file1'
with open("file1.txt") as file1:
    # This line is unnecessary as it just assigns the file object to 'contents_file_1'
    # It does not read the contents of the file. You can remove this line.
    contents_file_1 = file1
    # This will print the file object, not the contents. To print the contents, use file1.read()
    print(contents_file_1)

    # Read all lines from 'file1' and store them in 'file1_list'
    file1_list = file1.readlines()
    # Convert each line to an integer after stripping whitespace and store in 'numbers_f1'
    numbers_f1 = [int(n1.strip()) for n1 in file1_list]
    # Print the list of numbers extracted from 'file1'
    print(numbers_f1)

    # Alternative approach using a for loop (commented out)
    # numbers_f1 = []
    # for i in file1_list:
    #    numbers_f1.append(int(i.strip()))

# Open 'file2.txt' in read mode and assign the file object to 'file2'
with open("file2.txt") as file2:
    # This line is unnecessary as it just assigns the file object to 'contents_file_2'
    # It does not read the contents of the file. You can remove this line.
    contents_file_2 = file2
    # This will print the file object, not the contents. To print the contents, use file2.read()
    print(contents_file_2)

    # Read all lines from 'file2' and store them in 'file2_list'
    file2_list = file2.readlines()
    # Convert each line to an integer after stripping whitespace and store in 'numbers_f2'
    numbers_f2 = [int(n2.strip()) for n2 in file2_list]
    # Print the list of numbers extracted from 'file2'
    print(numbers_f2)

    # Alternative approach using a for loop (commented out)
    # numbers_f2 = []
    # for i in file2_list:
    #    numbers_f2.append(int(i.strip()))
    # print(numbers_f2)

# Find common numbers between 'numbers_f1' and 'numbers_f2' using a list comprehension
result = [n1 for n1 in numbers_f1 if n1 in numbers_f2]
# Print the result (common numbers)
print(result)

# Alternative approach using a for loop (commented out)
# result = []
# for n2 in numbers_f2:
#     if n2 in numbers_f1:
#         result.append(n2)
# print(result)

