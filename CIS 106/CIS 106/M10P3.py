def calculate_automobile_out_the_door_price(msrp, make, model, ev_code):
    discount_percent = 0.05  
    if make == 'Honda' and model == 'Accord':
        discount_percent = 0.10
    elif make == 'Toyota' and model == 'Rav4':
        discount_percent = 0.15
    elif ev_code == 'Y':
        discount_percent = 0.30
    
    discounted_price = msrp * (1 - discount_percent)
    total_price = discounted_price * 1.07 
    return total_price, msrp, discounted_price

def main():
    total_msrp = 0
    total_sales_price = 0
    
    while input("Do you want to calculate automobile price? (Yes/No): ").strip().lower() == 'yes':
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        ev_code = input("Is it an electric vehicle? (Y/N): ")
        msrp = float(input("Enter MSRP: "))
        total_price, msrp, discounted_price = calculate_automobile_out_the_door_price(msrp, make, model, ev_code)
        total_msrp += msrp
        total_sales_price += discounted_price
        print(f"Out the door price: {total_price}")
    
    print(f"Total MSRP of all cars: {total_msrp}")
    print(f"Total sales price of all cars: {total_sales_price}")

if __name__ == "__main__":
    main()
