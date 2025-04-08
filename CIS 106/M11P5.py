total = 0
tax = 0

def calculate_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * 0.07

def main():
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter unit price: "))
    
    calculate_total_and_tax(quantity, unit_price)
    
    print(f"Total: ${total:.2f}")
    print(f"Tax: ${tax:.2f}")

if __name__ == "__main__":
    main()
