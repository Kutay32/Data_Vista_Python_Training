import random

balance = 1000

def deal_card():
    return random.choice(["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

#if card is A add 11 if card is in (K, Q, J) add 10 otherwise add the numbers value for given list
def calculate_score(cards):
    score = sum([11 if card == "A" else 10 if card in ["K", "Q", "J"] else int(card) for card in cards])
    # if score > 21 subtract 10 from score. A can be 1 or 11
    if "A" in cards and score > 21:
        score -= 10
    return score

def compare(user_score, computer_score):
  if user_score == computer_score:
      return "It's a draw!"
  elif user_score > 21:
      return "You went over. You lose!"
  elif computer_score > 21:
      return "Opponent went over. You win!"
  elif user_score > computer_score:
      return "You win!"
  else:
      return "You lose!"

def show_balance():
    print(f"Your current balance: ${balance}")

def play_game():
    global balance
    bet = int(input("Place your bet: $"))

    if bet > balance:
        print("Bet amount exceeds your balance.")
        print(f"Your current balance: ${balance}")
        return

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    is_game_over = False

    #make a loop that will run until the round is over
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        print("----------")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, or 'n' to pass: ").lower()
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print("----------")
    result = compare(user_score, computer_score)
    print(result)
    print("----------")

    if "win" in result:
        balance += bet
        print(f"You won ${bet}! Your current balance: ${balance}")
    elif "lose" in result:
        balance -= bet
        print(f"You lost ${bet}. Your current balance: ${balance}")

# make a loop that will run until the user decides to quit
while True:
    print("\nWelcome to Blackjack!")
    print("1. Start Game")
    print("2. Show Balance")
    print("3. Quit")
    print("----------")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        play_game()
    elif choice == "2":
        show_balance()
    elif choice == "3":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
