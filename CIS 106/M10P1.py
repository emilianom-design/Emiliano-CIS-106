def forecast_sales(month, sales):
    forecast_percent = 0.0
    if month in ['Jan', 'Feb', 'Mar']:
        forecast_percent = 0.10
    elif month in ['Apr', 'May', 'Jun']:
        forecast_percent = 0.15
    elif month in ['Jul', 'Aug', 'Sep']:
        forecast_percent = 0.20
    elif month in ['Oct', 'Nov', 'Dec']:
        forecast_percent = 0.25
    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales

def main():
    while input("Do you want to forecast sales? (Yes/No): ").strip().lower() == 'yes':
        last_name = input("Enter last name: ")
        month = input("Enter month: ")
        sales = float(input("Enter sales: "))
        next_month_sales = forecast_sales(month, sales)
        print(f"Next month's forecast sales: {next_month_sales}")

if __name__ == "__main__":
    main()
