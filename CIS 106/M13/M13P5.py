import math

room_paint = {}

def calculate_paint_area(length, width, height):
    wall_area = 2 * height * (length + width)
    return math.ceil(wall_area / 50)

while True:
    name = input("Enter room name (or type 'done' to finish): ")
    if name.lower() == "done":
        break
    try:
        length = float(input("Length (feet): "))
        width = float(input("Width (feet): "))
        height = float(input("Height (feet): "))
    except ValueError:
        print("Please enter numeric values.")
        continue
    gallons = calculate_paint_area(length, width, height)
    room_paint[name] = gallons

print(f"\n{'Room':<10} {'Gallons Needed':<15}")
print("-" * 30)
for room, gallons in room_paint.items():
    print(f"{room:<10} {gallons:<15}")
