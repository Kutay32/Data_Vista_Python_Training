import random
import csv


def play_game():
    leaderboard_file = "leaderboard.csv"

   
    def load_scores():
        try:
            with open(leaderboard_file, mode="r") as file:
                return {
                    row[0]: int(row[1])
                    for row in csv.reader(file)
                    if len(row) == 2 and row[1].isdigit()
                }
        except FileNotFoundError:
            return {}

    
    def save_scores(scores):
        with open(leaderboard_file, mode="w") as file:
            writer = csv.writer(file)
            for name, score in scores.items():
                writer.writerow([name, score])

    scores = load_scores()
    name = input("Enter your nickname: ")
    score = scores.get(name, 0)
    print(f"Hello {name}, your current score is {score}.")

    levels = {"1": (10, 10), "2": (50, 25), "3": (100, 50)}
    choice = input("Choose difficulty: 1. Easy 2. Medium 3. Hard: ")
    if choice not in levels:
        print("Invalid choice, exiting.")
        return

    max_num, points = levels[choice]
    secret = random.randint(1, max_num)
    print(f"Guess a number between 1 and {max_num}.")

    for attempt in range(5):
        guess = int(input(f"Attempt {attempt + 1}/5: "))
        if guess == secret:
            print("Correct! You earned points.")
            score += points
            break
        elif guess < secret:
            print("Higher!")
        else:
            print("Lower!")
    else:
        print(f"Out of attempts! The number was {secret}.")

    scores[name] = score
    print(f"Your total score is now {score}.")
    save_scores(scores)

    if input("Play again? (yes/no): ").lower() == "yes":
        play_game()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    play_game()
