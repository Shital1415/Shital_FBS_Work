'''
6. Write a program to calculate profit or loss.
'''

cost_price = float(input("enter your product cost price"))
sell_price = float(input("enter your product selling price"))

if(sell_price > cost_price):
    profit = sell_price - cost_price
    print(f"you got the {profit} Rupees profit")
else:
    loss = cost_price - sell_price
    print(f"you have lost the {loss} Rupees ")