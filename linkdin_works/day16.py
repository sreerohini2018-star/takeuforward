
"""
SUM THE LIST:-

write a function called sum_list with one parametewr that takes a nested list of integers as an argument and returns  the4 sum of the integers. 
for example, if you pass [[2,4,5,6],[2,3,5,6]] as an argument your function should return a sum of 33. 
"""

def sum_list(numbers):
    total = 0

    for num in numbers:
        for n in num:
            total += n

    return total


print(sum_list([[2,4,5,6], [2,3,5,6]]))


