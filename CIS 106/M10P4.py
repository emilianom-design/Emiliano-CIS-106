def calculate_train_ticket_price(miles):
    if miles >= 30:
        ticket_price = 12
    elif miles >= 20:
        ticket_price = 10
    elif miles >= 10:
        ticket_price = 8
    else:
        ticket_price = 5
    return ticket_price

def main():
    total_train_ticket_price = 0
    while input("Do you want to calculate train ticket price? (Yes/No): ").strip().lower() == 'yes':
        miles = float(input("Enter miles from downtown Chicago: "))
        ticket_price = calculate_train_ticket_price(miles)
        total_train_ticket_price += ticket_price
        print(f"Train ticket price: {ticket_price}")
    
    print(f"Total train ticket price: {total_train_ticket_price}")

if __name__ == "__main__":
    main()
