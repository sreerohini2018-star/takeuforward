
"""
WORDS AND ELEMENTS:-
write two functions. the first function is called count_words which takes a string of words and counts how many words are in the string.
the second function is called count_elements takes a tring of words and counts how many elements are in the string. do not count the 
whitespaces. the first function will return the number of words in a string and the second one will return the number of elements (less
whitespaces). if you pass 'i love learning' the count_words function should return 3 words and count_elements should return 13 elements.
"""

def count_words(word):
    word=word.split()
    return len(word)

def count_elements(word):
    word=word.replace(" ", "")
    return len(word)


text = "i love learning"
print("Number of words:", count_words(text))      
print("Number of elements:", count_elements(text)) 