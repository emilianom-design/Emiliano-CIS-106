def CompExtPrice(qty,price):
    extprice = qty * price
    if extprice > 1000000.00:
        discount = extprice * 0.10
    else:
        discount = 0
    newExtPrice = extprice - discount
    return newExtPrice

totalextprice = 0.0
decision = input("Do you want to run this program? enter yes ").lower()
while decision[0] == "y":
    qty = int(input('Enter the number of items to purchase '))
    price = float(input('Enter the price per item '))
    Extprice = CompExtPrice(qty,price)
    print("Quantity  \tPrice  \tExtended price")
    print("{:6,d}\t\t{:4,.2f}\t\t{:6,.2f}".format(qty,price,Extprice))
    totalextprice = totalextprice + Extprice
    decision = input("Do you want to continue this program? enter yes ").lower()
print("The total price is: ${:6,.2f}".format(totalextprice))
