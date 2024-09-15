def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes

    num_bytes = input_gb * (1024**3)
    return num_bytes

# print(lab1Question1(10))
# print(lab1Question1(5))

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    if name == '':
        return None
    len(name) % 2 != 0 
    if len(name) % 2 != 0:
        return True
    elif len(name) % 2 ==0:
        return False

# print(lab1Question2('sofie'))
# print(lab1Question2('murrey'))
# print(lab1Question2(''))

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    if not input_string:
        return -1
    if input_number <= len(input_string):
        character_at = input_string[input_number]
    else:
        character_at = -1
    return character_at
# print(lab1Question3('hello VietNam', 10))
# print(lab1Question3('hello VietNam', 27))
# print(lab1Question3('', 2))

def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    
    list_of_nums = []
    file = open(file_name, 'r')
    information = file.readlines()
    for each_line in information:
        list_of_nums.append(int(each_line))
    return list_of_nums
# print(lab1Question4('github/test_file1.txt'))
# print(lab1Question4('github/test_file2.txt'))


def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    my_set = set(list_numbers)
    max_number = max(my_set, key = list_numbers.count)
    mode_of_list = max_number
    return mode_of_list
# print(lab1Question5([12,1,35,1,23,43]))

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    
    total = (quarters* 0.25) + (dimes* 0.10) + (nickels* 0.05) + (pennies* 0.01)
    return total
# print(lab1Question6(12,3,34,2))

## Example of calling a function to test these... 
# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.