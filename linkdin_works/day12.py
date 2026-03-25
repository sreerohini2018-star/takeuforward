
"""
COUNT THE DOTS:-

write a function called count_dots. this function takes a string seperated by dots as a 
parameter and counts how many dots are in the string. for example 'h.e.l.p.' should return
4 dots and 'he.lp.' should return 2 dots
"""
def count_dots(text):
    return text.count('.')

print(count_dots("h.e.l.p.")) 
print(count_dots("he.lp."))