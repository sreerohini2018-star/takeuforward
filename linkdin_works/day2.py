
"""
STRINGS TO INTEGERS:-

write a function called convert_add that takes a list of string as an argument and converts
it into integers and sums the list. for example, ['1','3','5'] should be converted to [1,3,5]
and summed to 9.
"""
def convert_add(lst):

    sum=0

    for l in lst:

        l=int(l)
        sum+=l

    return sum

print(convert_add(['1','3','5']))    
print(convert_add(['10','20','30']))