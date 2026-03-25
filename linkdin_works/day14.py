
"""
FLATTEN THE LIST:-
write a function called flat_list that takes one argument, a nested list. the function converts
the nested list into 1D list. for example, [[2,4,5,6]] should return [2,4,5,6].

TEACHERS SALARY:-
b) a school has asked you to write a program that will calculate teachers salaries. the program should ask the user
to enter the teachers name, the number of periods thaught in a month, and the rate per period. the monthly salary is calculated
by multiplying no:of periods by the monthly rate. the current monthly rate per period is $20. if a teacher has more than
100 periods in a month, everything above 100 is overtime. overtime is $25 per period. for example, if a teacher has thaught
105 periods, their monthly gross salary should be 2125. write a function called your salary that calculates a teachers gross
salary. the function should return the teachers name, periods thaught and gross salary. here is how you should format your output.
teacher: john kelly
periods: 105
gross salary: 2125

"""

def flat_list(my_list):
    flat = []
    for list in my_list:
        for l in list:
            flat.append(l)
    return flat
numbers = [[2,4,5,6]]
print(flat_list(numbers))

#teachers salary
def your_salary():
    name = input("Enter teacher name: ")
    periods = int(input("Enter number of periods: "))

    if periods <= 100:
        salary = periods * 20
    else:
        overtime = periods - 100
        salary = (100 * 20) + (overtime * 25)

    print("Teacher:", name)
    print("Periods:", periods)
    print("Gross salary:", salary)
your_salary()