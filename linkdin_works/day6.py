
"""
USER NAME GENERATOR:-

write a function called user_name that generates a username from the users email. the code
should ask the user to input an email and the code should return everything before the @
sign as their user name. for example, if someone enters ben@gmail.com, the code should 
return ben as their username.
"""

def user_name():

    email=input("enter the email: ")
    username=email.split("@")[0]

    return username

print(user_name())

