
"""
HIDE MY PASSWORD:-

write a function called hide_password that takes no parameters, the function takes an input (a password)
from a user and returns a hidden password. for example, if the user enters "hello" as a password the
function should return "****" as a password and tell the user that the password is 4 characters long.

EXTRA CHALLENGE:STRINGS WITH A THOUSAND SEPARATOR
b. your new company has a list of figures saved in a list. the issue  is that these numbers have no 
separator. the numbers are saved in the following format:
[1000000,2356989,2354672,9878098]
you have been asked to write a code that will convert each of the numbers in the list into a string.
your code should then add a comma on each number as a thousand separator for readability. when you
run your code on the above list, your output should be:
['1,000,000','2,356,989','2,354,672','9,878,098']
write a function called convert_numbers that will take one argument, a list of numbers above. 
"""

def hide_password():
    password = input("Enter your password: ")
    hidden = "*" * len(password)
    print(hidden)
    print("the Password is", len(password), "characters long")
hide_password()    
print("================================")

#STRINGS WITH A THOUSAND SEPARATOR
def convert_numbers(numbers):
    new_list = []
    for n in numbers:
        s = str(n)
        new_list.append(s[:-6] + "," + s[-6:-3] + "," + s[-3:])
    return new_list
numbers = [1000000, 2356989, 2354672, 9878098]
print(convert_numbers(numbers))
