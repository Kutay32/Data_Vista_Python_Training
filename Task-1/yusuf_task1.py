import random

# Kart destelerini, değerlerini ve isimlerini tanımlayalım
suits = ("Kalp", "Sinek", "Maça", "Karo")
ranks = ("İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz", "On", "Vale", "Kız", "Papaz", "As")
values = {'İki':2, 'Üç':3, 'Dört':4, 'Beş':5, 'Altı':6, 'Yedi':7, 'Sekiz':8, 'Dokuz':9, 'On':10, 'Vale':10,
         'Kız':10, 'Papaz':10, 'As':11}

class Kart:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " " + self.suit

class Deste:
    def __init__(self):
        self.deck = []  # Tüm kartları içeren liste
        for suit in suits:
            for rank in ranks:
                self.deck.append(Kart(suit, rank))
        self.karistir()

    def karistir(self):
        random.shuffle(self.deck)

    def dagit(self):
        return self.deck.pop()

# Oyuncu veya krupiyenin elini temsil eden sınıf
class El:
    def __init__(self):
        self.cards = []  # Elindeki kartlar
        self.deger = 0   # Elinin değeri
        self.aslar = 0    # As sayısı

    def kart_ekle(self, card):
        self.cards.append(card)
        self.deger += values[card.rank]
        if card.rank == 'As':
            self.aslar += 1

    def as_ayarla(self):
        while self.deger > 21 and self.aslar:
            self.deger -= 10
            self.aslar -= 1

# Oyunun ana döngüsü
def oyun():
    oyun_devam_ediyor = True

    # Yeni bir deste oluştur ve karıştır
    deste = Deste()
    deste.karistir()

    # Oyuncu ve krupiye için yeni eller oluştur
    oyuncu_eli = El()
    krupiye_eli = El()

    # Her birine ikişer kart dağıt
    for i in range(2):
        oyuncu_eli.kart_ekle(deste.dagit())
        krupiye_eli.kart_ekle(deste.dagit())

    # Oyuncunun hamleleri
    while oyun_devam_ediyor:
        print("\nElinizdeki kartlar:")
        for card in oyuncu_eli.cards:
            print(card)
        print("Elinizin değeri:", oyuncu_eli.deger)

        # Oyuncunun hit veya stand seçmesi
        hamle = input("Kart çekmek için 'c' veya durmak için 'd' tuşuna basın: ")
        if hamle.lower() == 'c':
            oyuncu_eli.kart_ekle(deste.dagit())
            if oyuncu_eli.deger > 21:
                print("Elinizin değeri 21'i geçti. Kaybettiniz.")
                oyun_devam_ediyor = False
        elif hamle.lower() == 'd':
            oyun_devam_ediyor = False
        else:
            print("Geçersiz giriş. Lütfen 'c' veya 'd' tuşuna basın.")

    # Krupiyenin hamleleri
    if oyuncu_eli.deger <= 21:
        while krupiye_eli.deger < 17:
            krupiye_eli.kart_ekle(deste.dagit())

        # Kazananı belirle
        print("\nKrupiyenin eli:")
        for card in krupiye_eli.cards:
            print(card)
        print("Krupiyenin değeri:", krupiye_eli.deger)

        if krupiye_eli.deger > 21:
            print("Krupiyenin eli 21'i geçti. Kazandınız!")
        elif oyuncu_eli.deger > krupiye_eli.deger:
            print("Kazandınız!")
        elif oyuncu_eli.deger < krupiye_eli.deger:
            print("Kaybettiniz.")
        else:
            print("Berabere!")

oyun()