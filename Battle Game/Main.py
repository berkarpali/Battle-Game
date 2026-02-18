from character import Character

p1 = Character("Knight", 100, 20)
p2 = Character("Orc", 80, 15)

while p1.is_alive() and p2.is_alive():

    print("\n1- Knight attack")
    print("2- Orc attack")
    print("3- Show status")
    print("4- exit")

    secim = input("Choice: ")

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
        print("İnvalid choice")

if not p1.is_alive():
    print("Knight is dead, Orc has won!")

if not p2.is_alive():
    print("Orc is dead, Knight has won!")

