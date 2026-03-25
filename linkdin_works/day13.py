
"""
PAY YOUR TAX:-

write a function called your_vat. the function takes no parameter. the function asks the user to input the price
of an item and VAT (vat should be a percentage). the function should return the price of the item plus VAT. if the
price is 220 and, VAT is 15% your code should return a vat inclusive price of 253. make sure that your code can handle value
error. ensure the code runs until valid numbers are entered (hint: your code should include a while loop).
"""


def your_vat():
    while True:
        try:
            price = float(input("Enter item price: "))
            vat = float(input("Enter VAT percentage: "))

            if price >= 0 and vat >= 0:
                total = price + (price * vat / 100)
                return total
            else:
                print("Price and VAT must be positive numbers.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

result = your_vat()
print("Price including VAT:", result)