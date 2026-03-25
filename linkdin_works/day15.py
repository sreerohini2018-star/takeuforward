
"""
SAME IN REVERSE:-

write a function called same_in_reverse that takes a string and checks if the string reads the same in reverse. if it is the same,
it should return true. if not, it should return false. for example, 'dad' should return true, because it reads the same in reverse.
"""

def same_in_reverse(word):
    return word==word[::-1]

print(same_in_reverse('dad'))
print(same_in_reverse('father'))