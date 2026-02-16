from character import Character

p1 = Character("Knight", 100, 20)
p2 = Character("Orc", 80, 15)

while p1.is_alive() and p2.is_alive():

    print("\n1- Knight saldır")
    print("2- Orc saldır")
    print("3- Durumu göster")
    print("4- Çık")

    secim = input("Seçim: ")

    if secim == "1":
        p1.attack(p2)

    elif secim == "2":
        p2.attack(p1)

    elif secim == "3":
        p1.show_status()
        p2.show_status()

    elif secim == "4":
        break

    else:
        print("Geçersiz seçim")

if not p1.is_alive():
    print("Knight öldü! Orc kazandı!")

if not p2.is_alive():
    print("Orc öldü! Knight kazandı!")
