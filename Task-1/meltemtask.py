import random


card_values = {
    "A": [1, 11],
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10
}


player_balance = 1000


def deal_card():
    return random.choice(list(card_values.keys()))


def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        if card == "A":
            ace_count += 1
        else:
            score += card_values[card]

    
    for _ in range(ace_count):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1

    return score


def blackjack_game():
    global player_balance, games_won, games_lost
    print("\nStarting a new game of Blackjack!")
    if player_balance <= 0:
        print("You don't have enough money to play. Game over!")
        return

    bet = int(input(f"Enter your bet (You have ${player_balance}): "))
    if bet > player_balance:
        print("You cannot bet more than your current balance!")
        return


    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")

   
    while True:
        choice = input("Type 'hit' to get another card, or 'stand' to pass: ").lower()
        if choice == "hit":
            player_hand.append(deal_card())
            print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
            if calculate_score(player_hand) > 21:
                print("You went over. You lose!")
                player_balance -= bet
                
                return
        elif choice == "stand":
            break
        else:
            print("Invalid choice, please type 'hit' or 'stand'.")

  
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    print(f"Dealer's cards: {dealer_hand}, dealer's score: {calculate_score(dealer_hand)}")

    
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
        player_balance += bet
     
    elif player_score == dealer_score:
        print("It's a draw!")
    else:
        print("You lose!")
        player_balance -= bet
      


def show_balance():
    print(f"\nCurrent Balance: ${player_balance}")
  

def game_enter():
    while True:
        print("\nWelcome to Blackjack!")
        print("1. Start Game")
        print("2. Show Balance")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            blackjack_game()
        elif choice == "2":
            show_balance()
        elif choice == "3":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

game_enter()
