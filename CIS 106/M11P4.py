def calculate_scores_with_handicap(score1, score2, score3, handicap):
    average_score = (score1 + score2 + score3) / 3
    average_score_with_handicap = average_score + handicap
    return average_score, average_score_with_handicap

def main():
    last_name = input("Enter bowler's last name: ")
    score1 = float(input("Enter first game score: "))
    score2 = float(input("Enter second game score: "))
    score3 = float(input("Enter third game score: "))
    handicap = float(input("Enter bowling handicap: "))
    
    average_score, average_score_with_handicap = calculate_scores_with_handicap(score1, score2, score3, handicap)
    
    print(f"Bowler: {last_name}")
    print(f"Average score: {average_score:.2f}")
    print(f"Average score with handicap: {average_score_with_handicap:.2f}")

if __name__ == "__main__":
    main()
