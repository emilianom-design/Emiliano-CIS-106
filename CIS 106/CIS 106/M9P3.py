def compute_mpg(miles, gallons):
    if gallons == 0:  
        return 0
    return miles / gallons

def trip_main():
    trip_count = 0
    while True:
        destination = input("Enter destination city (or 'done' to stop): ")
        if destination.lower() == 'done':
            break

        miles = float(input(f"Enter miles traveled to {destination}: "))
        gallons = float(input(f"Enter gallons used for the trip to {destination}: "))

        mpg = compute_mpg(miles, gallons)
        print(f"Destination: {destination} | Miles: {miles} | MPG: {mpg:.2f}")

        trip_count += 1

    print(f"Total trips entered: {trip_count}")

trip_main()
