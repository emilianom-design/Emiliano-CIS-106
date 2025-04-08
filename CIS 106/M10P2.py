def calculate_wall_square_footage(length, width, height):
    return 2 * length * height + 2 * width * height

def calculate_gallons_needed(wall_square_footage):
    return wall_square_footage / 50

def main():
    while input("Do you want to calculate paint for room? (Yes/No): ").strip().lower() == 'yes':
        length = float(input("Enter length of room: "))
        width = float(input("Enter width of room: "))
        height = float(input("Enter height of room: "))
        wall_square_footage = calculate_wall_square_footage(length, width, height)
        gallons_needed = calculate_gallons_needed(wall_square_footage)
        print(f"Gallons of paint needed: {gallons_needed}")
        
        ceiling_area = length * width
        print(f"Ceiling area: {ceiling_area} square feet")
        varnish_needed = ceiling_area / 50
        print(f"Gallons of varnish needed for ceiling: {varnish_needed}")

if __name__ == "__main__":
    main()
