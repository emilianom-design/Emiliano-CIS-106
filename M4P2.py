#input
purchase_price = float(input("Enter the purchase price per share: $"))
current_price = float(input("Enter the current stock price: $"))
quantity = int(input("Enter the quantity of stock: "))

#Process phase
Stock_value_change = (current_price - purchase_price) * quantity

#Output
print("the change in value of your stock price is", "{:.2f}". format(Stock_value_change))
