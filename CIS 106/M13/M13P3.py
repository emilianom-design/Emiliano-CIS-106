filename = "players2.txt"
player_dict = {}

try:
    with open(filename, "r") as file:
        for line in file:
            name, avg = line.strip().split()
            player_dict[name] = float(avg)
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    exit()

print(f"{'Player':<10} {'Average':<6}")
print("-" * 20)
for name, avg in player_dict.items():
    print(f"{name:<10} {avg:.3f}")
