import random

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def calculate_score(hand):
    score = 0
    for card in hand:
        if card in ['J', 'K', 'Q']:
            score += 10
        elif card == 'A':
            score += 11 if score + 11 <= 21 else 1
        else:
            score += int(card)
    return score

balance = 1000

def bj_game():
    global balance
    print("\nwelcome to blackjack")
    print(f"your current balance: {balance}")
    bet = int(input("place your bet: "))

    if bet > balance or bet <= 0:
        print("invalid bet amount")
        return

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    while True:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"\nyour cards: {player_hand}, current score: {player_score}")
        print(f"dealer s first card: {dealer_hand[0]}")

        if player_score > 21:
            print("you went over 21, you lose")
            balance -= bet
            break

        choice = input("type 'hit' to get another card, or 'stand' to pass: ").lower()
        if choice == 'hit':
            player_hand.append(deal_card())
        else:
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(deal_card())
                dealer_score = calculate_score(dealer_hand)

            print(f"\nyour final hand: {player_hand}, final score: {player_score}")
            print(f"dealer s final hand: {dealer_hand}, final score: {dealer_score}")

            if dealer_score > 21 or player_score > dealer_score:
                print("you win")
                balance += bet
            elif dealer_score == player_score:
                print("draw")
            else:
                print("you lose")
                balance -= bet
            break

    print(f"your current balance: {balance}")

def menu():
    global balance
    print("welcome to the blackjack game")
    while balance > 0:
        print("\n1 start game")
        print("2 show balance")
        print("3 quit")
        choice = input("enter your choice (1,2,3) ")

        if choice == '1':
            bj_game()
        elif choice == '2':
            print(f"your current balance: {balance}")
        elif choice == '3':
            print("thanks for playing")
            break
        else:
            print("invalid choice, please try again.")
    else:
        print("you are out of money, Game over.")

menu()
