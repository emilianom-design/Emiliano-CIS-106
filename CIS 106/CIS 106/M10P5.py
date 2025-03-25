def calculate_assessed_value(county, market_value):
    assessed_value_percent = 0.7  
    if county == 'Cook':
        assessed_value_percent = 0.90
    elif county == 'DuPage':
        assessed_value_percent = 0.80
    elif county == 'McHenry':
        assessed_value_percent = 0.75
    elif county == 'Kane':
        assessed_value_percent = 0.60
    
    assessed_value = market_value * assessed_value_percent
    return assessed_value

def main():
    total_market_value = 0
    total_assessed_value = 0
    while input("Do you want to calculate home assessed value? (Yes/No): ").strip().lower() == 'yes':
        county = input("Enter county: ")
        market_value = float(input("Enter market value of home: "))
        assessed_value = calculate_assessed_value(county, market_value)
        total_market_value += market_value
        total_assessed_value += assessed_value
        print(f"Assessed value: {assessed_value}")
    
    print(f"Total market value of all homes: {total_market_value}")
    print(f"Total assessed value of all homes: {total_assessed_value}")

if __name__ == "__main__":
    main()
