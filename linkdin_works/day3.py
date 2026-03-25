
"""
REGISTER CHECK:-

write a function called register_check that checks how many students are in school. the function takes a dictionary
as a parameter.if the student is in school , the dictionary says 'yes'. if the student is not in school, the dictionary says 'no'.
your function should return the number of students in school.use the dictionary below.your function should return 3.
register={'michael':'yes','john':'no','peter':'yes','mary':'yes'}
"""

def register_check(register):
    
    students_in_school={k:v for k,v in register.items() if v=='yes'}
    return len(students_in_school)

register={'michael':'yes','john':'no','peter':'yes','mary':'yes','hari':'yes','abhi':'no','sree':'yes'}
print(register_check(register))