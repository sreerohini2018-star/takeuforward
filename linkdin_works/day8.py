
"""
ODD AND EVEN:-

write a function called odd_even that has only one parameter and takes a list of numbers as 
an argument. the function returns the difference between the largest even number in the list
and the smallest odd number in the list. for example, if you pass [1,2,4,6] as an argument
the function should return 6-1=5.

"""
def odd_even(numbers):
    evens = [num for num in numbers if num%2==0]
    odds = [num for num in numbers if num%2!=0]

    largest_even_num=max(evens)
    smallest_odd_num=min(odds)

    return largest_even_num-smallest_odd_num

print(odd_even([1,2,4,6]))
print(odd_even([5,2,8,6,15]))
