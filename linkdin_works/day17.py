
"""
USERNAME GENERATOR:-

write a function called user_name, that creates a username for the user. the function should ask a user to 
input their name. the function should then reverse the name and attach a randomly issued number between 0-9 at the end of the name. 
the function should return the username
"""

import random

def user_name():
    
    name = input("Enter your name: ")
    
    reversed_name = name[::-1]
    
    random_number = random.randint(0, 9)
    
    username = reversed_name + str(random_number)
    
    return username

username = user_name()
print("Your username is:", username)