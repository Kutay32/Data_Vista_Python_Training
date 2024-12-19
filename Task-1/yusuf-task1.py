import random

# Kart destesi ve değerleri
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": (1, 11)
}
CARD_DECK = list(CARD_VALUES.keys()) * 4

# Oyuncu sınıfı
class Player:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.hand = []

    def calculate_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            if card == "A":
                aces += 1
                score += 11
            else:
                score += CARD_VALUES[card]
        
        # Aşım kontrolü için Asları ayarla
        while score > 21 and aces:
            score -= 10
            aces -= 1
        
        return score

    def add_card(self, card):
        self.hand.append(card)

# Blackjack menüsü
def show_menu():
    print("\nBlackjack oyununa hoş geldiniz!")
    print("1. Oyunu Başlat")
    print("2. Bakiye Görüntüle")
    print("3. Çıkış Yap")
    print("--------")
    choice = input("Seçiminizi yapın (1/2/3): ")
    return choice

# Oyunun ana akışı
def blackjack():
    print("Blackjack oyununa hoş geldiniz!")
    name = input("Adınızı girin: ")
    starting_balance = 100  # Başlangıç bakiyesi

    while True:
        # Oyuncunun başlangıç bakiyesi her yeni oyun için sıfırlanır
        player = Player(name, starting_balance)

        choice = show_menu()
        if choice == "1":
            print(f"\nYeni oyun başlatıldı! Bakiyeniz: {player.balance} TL")
            try:
                bet = int(input("Bahis miktarını girin: "))
                if bet > player.balance or bet <= 0:
                    print("Geçersiz bahis miktarı!")
                    continue
            except ValueError:
                print("Lütfen geçerli bir sayı girin!")
                continue

            # Kartları karıştır ve başlangıç ellerini dağıt
            random.shuffle(CARD_DECK)
            player.hand = [random.choice(CARD_DECK) for _ in range(2)]
            dealer_hand = [random.choice(CARD_DECK) for _ in range(2)]

            print(f"\n{player.name}'in kartları: {player.hand} (Skor: {player.calculate_score()})")
            print(f"Krupiyenin açık kartı: {dealer_hand[0]}")

            # Oyuncu hareketi
            while True:
                action = input("Hareket seç (kart çek/pas geç): ").lower()
                if action == "kart çek":
                    player.add_card(random.choice(CARD_DECK))
                    print(f"Yeni kartınız: {player.hand[-1]}")
                    print(f"Güncel skorunuz: {player.calculate_score()}")
                    if player.calculate_score() > 21:
                        print("Bust! Kaybettiniz.")
                        player.balance -= bet
                        break
                elif action == "pas geç":
                    break
                else:
                    print("Geçersiz seçim! Lütfen 'kart çek' veya 'pas geç' yazın.")
            
            # Krupiyenin hareketi
            if player.calculate_score() <= 21:
                print("\nKrupiye oynuyor...")
                while sum(CARD_VALUES[card] if card != "A" else 11 for card in dealer_hand) < 17:
                    dealer_hand.append(random.choice(CARD_DECK))
                
                dealer_score = sum(CARD_VALUES[card] if card != "A" else 11 for card in dealer_hand)
                print(f"Krupiyenin kartları: {dealer_hand} (Skor: {dealer_score})")

                # Kazanan belirleme
                if dealer_score > 21 or player.calculate_score() > dealer_score:
                    print("Tebrikler! Kazandınız.")
                    player.balance += bet
                elif player.calculate_score() < dealer_score:
                    print("Krupiye kazandı!")
                    player.balance -= bet
                else:
                    print("Beraberlik!")

        elif choice == "2":
            print(f"Mevcut bakiyeniz: {player.balance} TL")

        elif choice == "3":
            print("Oyundan çıkılıyor. Görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")

# Oyunu başlat
if __name__ == "__main__":
    blackjack()
