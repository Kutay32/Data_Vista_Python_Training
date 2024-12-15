import random

def random_number(diff):
    if diff == "easy":
        return random.randint(1,10), 10
    elif diff == "medium":
        return random.randint(1,50), 50
    elif diff == "hard":
        return random.randint(1,100), 100
    else:
        return None, 0

def hint(target):
    if target % 2 == 0:
        return "hint: the number is even"
    else:
        return "hint: the number is odd"

def play_game():
    print("welcome to the number guessing game")

    nickname = input("enter your nickname: ")

    print("choose a difficulty: easy, medium, hard")
    difficulty = input("your choice: ").lower()

    if difficulty not in ["easy", "medium", "hard"]:
        print("invalid difficulty. exiting game")
        return

    target, points = random_number(difficulty)
    print(f"great, you have chosen [difficulty] mode. ")

    attempts = 5
    hint_used = False
    while attempts > 0:
        try:
            guess = int(input(f"guess the number (Attempts left: {attempts}):"))
            if guess == target:
                print(f"congratulations {nickname}, you guessed it right. you earned {points} points.")
                return
            elif guess < target:
                print("higher")
            else:
                print("lower")

            if not hint_used:
                use_hint = input("would you like a hint? (yes or no): ").lower()
                if use_hint == "yes":
                    print(hint(target))
                    hint_used = True

        except ValueError:
            print("please enter a valid number")

        attempts -= 1

    print(f"sorry, you're out of attempts, the correct number was {target}."),

play_game()