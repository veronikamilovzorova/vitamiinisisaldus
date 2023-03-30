import random

def patsiendid():
    nimed = []
    D_vitamiini_sisaldus = []
    n = int(input("Sisestage patsientide arv: "))
    
    for i in range(n):
        nimi = input(f"Sisestage nimi {i+1}- patsienti: ")
        nimed.append(nimi)
        D_vitamiini_sisaldus.append(random.randint(10, 50))
    
    while True:
        print("\nValige tegevus:")
        print("1. Tehke nimekiri patsientidest, kellel on vitamiinipuudus D (<30)")
        print("2. Leida keskmine vitamiin D")
        print("3. Kuvage K kõrgeima punktisumma saanud inimese loend")
        print("4. Otsida patsiente nime järgi")
        print("5. Lisada uus patsient")
        print("6. Programmist väljumine")
        choice = input("Teie valik: ")
        
        if choice == '1':
            print("Vitamiinipuudusega patsientide nimekiri D (<30):")
            for i in range(len(nimed)):
                if D_vitamiini_sisaldus[i] < 30:
                    print(f"{nimed[i]} - {D_vitamiini_sisaldus[i]}")
        
        elif choice == '2':
            avg_D = sum(D_vitamiini_sisaldus) / n
            print(f"Keskmine vitamiiniarv D: {avg_D}")
        
        elif choice == '3':
            k = int(input("Sisestage kuvatavate patsientide arv: "))
            sorted_indices = sorted(range(len(D_vitamiini_sisaldus)), key=lambda i: D_vitamiini_sisaldus[i], reverse=True)
            print(f"Järjend {k} kõrgeima vitamiinisisaldusega patsiendid D:")
            for i in range(k):
                print(f"{nimed[sorted_indices[i]]} - {D_vitamiini_sisaldus[sorted_indices[i]]}")
        
        elif choice == '4':
            query = input("Sisestage patsiendi nimi: ")
            matches = [i for i, name in enumerate(nimed) if query in name]
            if len(matches) > 0:
                print(f"Leidnud {len(matches)} patsienti:")
                for i in matches:
                    print(f"{nimed[i]} - {D_vitamiini_sisaldus[i]}")
            else:
                print("Patsiente ei leitud")
        
        elif choice == '5':
            n += 1
            nimi = input(f"Sisestage {n} patsienti: ")
            nimed.append(nimi)
            D_vitamiini_sisaldus.append(random.randint(10, 50))
            print("Uus patsient on edukalt lisatud")
        
        elif choice == '6':
            print("Programmist väljumine")
            break
        
patsiendid()
