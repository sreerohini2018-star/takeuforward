
"""
BIGGEST ODD NUMBER:-

create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in
the list. for example, if you pass '23569' as an argument, your function should return 9. use list comprehension
"""
def biggest_odd(numbers):

    odds = [int(num) for num in numbers if int(num) % 2 != 0]

    return max(odds)
print(biggest_odd('23569'))
print(biggest_odd('8237'))

