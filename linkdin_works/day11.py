
"""
ARE THEY EQUAL?
write a function called equal_strings. the function takes two strings as arguments and compare them.
if the strings are equal (if they have the same characters and have equal length) it should return
true, if they are not, it should return false. for example, 'love' and 'evol' should return true.

"""
def equal_strings(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    return sorted(str1) == sorted(str2)
print(equal_strings('love', 'evol'))  
print(equal_strings('hello', 'bello')) 
print(equal_strings('cat', 'tac')) 


