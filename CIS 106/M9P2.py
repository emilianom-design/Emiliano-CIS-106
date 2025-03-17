def compute_batting_average(hits, at_bats):
    if at_bats == 0:  
        return 0
    return hits / at_bats

def main():
    player_count = 0
    while True:
        last_name = input("Enter player's last name (or 'end' to stop): ")
        if last_name.lower() == 'end':
            break

        hits = int(input(f"Enter number of hits for {last_name}: "))
        at_bats = int(input(f"Enter number of at bats for {last_name}: "))

        batting_avg = compute_batting_average(hits, at_bats)
        print(f"{last_name}'s batting average is {batting_avg:.3f}")
        
        player_count += 1

    print(f"Total players entered: {player_count}")

main()
