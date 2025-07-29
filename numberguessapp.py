import random

def sayi_tahmin_oyunu():
    print("=== Sayı Tahmin Oyununa Hoş Geldin! ===")
    alt_sinir = 1
    ust_sinir = 100
    dogru_sayi = random.randint(alt_sinir, ust_sinir)
    tahmin_sayisi = 0

    while True:
        try:
            tahmin = int(input(f"{alt_sinir} ile {ust_sinir} arasında bir sayı tahmin et: "))
            tahmin_sayisi += 1

            if tahmin < alt_sinir or tahmin > ust_sinir:
                print("Lütfen belirtilen aralıkta bir sayı gir.")
            elif tahmin < dogru_sayi:
                print("Daha büyük bir sayı dene.")
            elif tahmin > dogru_sayi:
                print("Daha küçük bir sayı dene.")
            else:
                print(f"Tebrikler! {tahmin_sayisi} denemede doğru tahmini yaptın. Doğru sayı: {dogru_sayi}")
                break
        except ValueError:
            print("Geçerli bir sayı girmelisin.")

if __name__ == "__main__":
    sayi_tahmin_oyunu()
