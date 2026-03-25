
"""
A STRING RANGE:-

write a function called string_range that takes a single number and returns a string
of its range. the string characters should be seperated by dots(.).for example, 
if you pass 6 as an argument, your function should return '0.1.2.3.4.5'.
"""

def string_range(num):
    result=""
    for i in range(num):
        result+=str(i)
        if i!=num-1:
            result+="."
    return result
print(string_range(6))    