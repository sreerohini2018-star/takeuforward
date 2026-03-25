
"""
ANY NUMBER OF ARGUMENTS:-

write a function called any_number that can recieve any number of arguments(integers and floats) and return the average of 
those integers. if you pass 12,90,12,34 as arguments your function should return 37.0 as average. if you pass 12,90 your
function should return 51.0 as average.
"""

def any_number(*nums):
    return sum(nums) / len(nums)


print(any_number(12, 90, 12, 34))  
print(any_number(12, 90))          