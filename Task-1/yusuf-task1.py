import random

class Kart:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " " + self.suit

class Deste:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Kart(suit, rank))
        self.karistir()

    def karistir(self):
        random.shuffle(self.deck)

    def dagit(self):
        return self.deck.pop()

class El:
    def __init__(self):
        self.cards = []
        self.deger = 0
        self.aslar = 0

    def kart_ekle(self, card):
        self.cards.append(card)
        self.deger += values[card.rank]
        if card.rank == 'As':
            self.aslar += 1

    def as_ayarla(self):
        while self.deger > 21 and self.aslar:
            self.deger -= 10
            self.aslar -= 1

suits = ("Kalp", "Sinek", "Maça", "Karo")
ranks = ("İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz", "On", "Vale", "Kız", "Papaz", "As")
values = {'İki':2, 'Üç':3, 'Dört':4, 'Beş':5, 'Altı':6, 'Yedi':7, 'Sekiz':8, 'Dokuz':9, 'On':10, 'Vale':10,
         'Kız':10, 'Papaz':10, 'As':11}

def oyun():
    isim = input("Adınızı giriniz: ")
    para = 100  # Başlangıç parası
    toplam_kazanc = 0
    while para > 0:
        print(f"{isim}, paranız: {para} TL")
        bahis = int(input("Bahsinizi girin: "))

        while bahis > para:
            print("Yetersiz bakiye. Lütfen daha düşük bir bahis girin.")
            bahis = int(input("Bahsinizi girin: "))

        # Yeni bir deste oluştur ve karıştır
        deste = Deste()
        deste.karistir()

        # Oyuncu ve krupiye için yeni eller oluştur
        oyuncu_eli = El()
        krupiye_eli = El()

        # Her birine ikişer kart dağıt
        for _ in range(2):
            oyuncu_eli.kart_ekle(deste.dagit())
            krupiye_eli.kart_ekle(deste.dagit())

        # Oyuncunun hamleleri
        while True:
            print("\nElinizdeki kartlar:")
            for card in oyuncu_eli.cards:
                print(card)
            print("Elinizin değeri:", oyuncu_eli.deger)

            hamle = input("Kart çekmek için 'c', durmak için 'd' veya oyunu bırakmak için 'q' tuşuna basın: ")
            if hamle.lower() == 'c':
                oyuncu_eli.kart_ekle(deste.dagit())
                if oyuncu_eli.deger > 21:
                    print("Elinizin değeri 21'i geçti. Kaybettiniz.")
                    break
            elif hamle.lower() == 'd':
                break
            elif hamle.lower() == 'q':
                print("Oyunu bıraktınız.")
                return
            else:
                print("Geçersiz giriş.")

        # Oyuncu 21'i geçmediyse krupiye oynamaya devam eder
        if oyuncu_eli.deger <= 21:
            # Krupiyenin hamleleri (önceki kodlardan aynı)

            # Kazananı belirle ve parayı güncelle
            if krupiye_eli.deger > 21:
                print("Kazandınız!")
                para += bahis
                toplam_kazanc += bahis
            elif oyuncu_eli.deger > krupiye_eli.deger:
                print("Kazandınız!")
                para += bahis
                toplam_kazanc += bahis
            elif oyuncu_eli.deger < krupiye_eli.deger:
                print("Kaybettiniz.")
                para -= bahis
            else:
                print("Berabere.")

        devam = input("Oyunu devam ettirmek ister misiniz? (e/h): ")
        if devam.lower() != 'e':
            break

    print(f"{isim}, toplam kazancınız: {toplam_kazanc} TL")
    print("Oyun bitti.")

oyun()