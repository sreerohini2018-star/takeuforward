
"""
MY DISCOUNT:-

create a function called my_discount. the function takes no arguments but asks the user to input the price 
and the discount(percentage) of the product. once the user inputs the price and discount, it calculates 
the price after the discount. the function should return the price after the discount. 
for example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.
"""

def my_discount():
    actual_price=int(input("enter the price: "))
    discount=int(input("enter the discount in percentage: "))

    discount_price=actual_price * (discount/100)
    final_price=actual_price - discount_price

    return final_price
print(my_discount())
