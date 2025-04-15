# ---------- PART 1 & 2: Basic Arrays and Display Functions ----------

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
scores = [87, 93, 78, 85, 92, 88, 80, 76, 90, 95]

def display_names_scores(names, scores):
    print("Names and Scores:")
    for i in range(len(names)):
        print(f"{names[i]} - {scores[i]}")

def display_names_scores_reverse(names, scores):
    print("Names and Scores in Reverse:")
    for i in range(len(names)-1, -1, -1):
        print(f"{names[i]} - {scores[i]}")

# ---------- PART 3: Load from File and Find High/Low Scores ----------

def load_students_from_file(filename):
    names = []
    scores = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            names.append(parts[0])
            scores.append(int(parts[1]))
    return names, scores

def display_high_low(names, scores):
    high_score = 0
    low_score = 999
    high_index = 0
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
            high_index = i
        if scores[i] < low_score:
            low_score = scores[i]
            low_index = i

    print(f"Highest Score: {names[high_index]} - {high_score}")
    print(f"Lowest Score: {names[low_index]} - {low_score}")

# ---------- PART 4 & 5: Players and Batting Averages ----------
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", 
              "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
scores = [87, 93, 78, 85, 92, 88, 80, 76, 90, 95]

def display_names_scores(names, scores):
    print("Names and Scores:")
    for i in range(len(names)):
        print(f"{names[i]} - {scores[i]}")

def display_names_scores_reverse(names, scores):
    print("Names and Scores in Reverse:")
    for i in range(len(names) - 1, -1, -1):
        print(f"{names[i]} - {scores[i]}")

def load_students_from_file(filename):
    names = []
    scores = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    names.append(parts[0])
                    scores.append(int(parts[1]))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return names, scores

def display_high_low(names, scores):
    if not scores:
        print("No scores to evaluate.")
        return

    high_score = 0
    low_score = 999
    high_index = 0
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_score:
            high_score = scores[i]
            high_index = i
        if scores[i] < low_score:
            low_score = scores[i]
            low_index = i

    print(f"Highest Score: {names[high_index]} - {high_score}")
    print(f"Lowest Score: {names[low_index]} - {low_score}")

def load_players_from_file(filename):
    names = []
    averages = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    names.append(parts[0])
                    averages.append(float(parts[1]))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return names, averages

def display_players(names, averages):
    print("Player Batting Averages:")
    for i in range(len(names)):
        print(f"{names[i]} - {averages[i]:.3f}")

def search_player(names, averages, search_name):
    if search_name in names:
        index = names.index(search_name)
        print(f"Found: {names[index]} - {averages[index]:.3f}")
    else:
        print("Name not found.")

display_names_scores(last_names, scores)
print()
display_names_scores_reverse(last_names, scores)
print()

student_names, student_scores = load_students_from_file("students.txt")
if student_names:
    display_names_scores(student_names, student_scores)
    print()
    display_high_low(student_names, student_scores)
    print()

player_names, batting_averages = load_players_from_file("players.txt")
if player_names:
    display_players(player_names, batting_averages)
    print()

    while True:
        search = input("Enter a player last name to search (or 'exit' to quit): ")
        if search.lower() == 'exit':
            break
        search_player(player_names, batting_averages, search)
