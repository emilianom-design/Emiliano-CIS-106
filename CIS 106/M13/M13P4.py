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

while True:
    search = input("Enter player name to look up (or type 'exit' to stop): ")
    if search.lower() == "exit":
        break
    if search in player_dict:
        print(f"{search} has a batting average of {player_dict[search]:.3f}")
    else:
        print(f"{search} not found.")
