def calculate_discount(price, discount_rate):
    discount_amount = price * discount_rate
    discount_price = price - discount_amount
    return discount_amount, discount_price

def main():
    quantity = int(input("enter quantity: "))
    price = float(input("enter price: "))
    discount_rate = float(input("enter discount rate in decimal form: "))

    discount_amount, discount_price = calculate_discount(price, discount_rate)

    print(f"Quantity: {quantity}")
    print(f"Price: ${price:.2f}")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Discounted price: ${discount_price:.2f}")

if __name__ == "__main__":
    main()
