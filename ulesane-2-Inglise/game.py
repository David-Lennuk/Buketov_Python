import random
import time

player = {
    "health": 100,
    "energy": 100,
    "food": 3,
    "hours_left": 12
}

def show_status():
    print("\n Mängija seisund:")
    print(f" Tervis: {player['health']}")
    print(f" Energia: {player['energy']}")
    print(f" Toidukogus: {player['food']}")
    print(f" Allesjäänud aeg: {player['hours_left']}h\n")

def rest():
    if player["food"] > 0:
        print(" Sa puhkasid ja sõid veidi toitu.")
        player["energy"] += 20
        player["health"] += 10
        player["food"] -= 1
    else:
        print(" Sul pole piisavalt toitu!")
        player["energy"] -= 10
    player["hours_left"] -= 1

def explore():
    print("🚶 Sa liigud edasi...")
    player["energy"] -= 30
    player["hours_left"] -= 1

def skip_time():
    print("🕰️ Sa otsustasid lihtsalt oodata...")
    player["energy"] -= 5
    player["hours_left"] -= 1

def game_loop():
    while player["hours_left"] > 0 and player["health"] > 0:
        show_status()
        print(" Mida soovid teha?")
        print("1. Puhka ja söö")
        print("2. Uuri ümbrust")
        print("3. Oota")
        choice = input("Vali tegevus (1-3): ")

        if choice == "1":
            rest()
        elif choice == "2":
            explore()
        elif choice == "3":
            skip_time()
        else:
            print(" Vigane valik!")

        if player["energy"] <= 0:
            print(" Sul sai energia otsa! Kaotad tervist.")
            player["health"] -= 20
            player["energy"] = 0

    if player["health"] <= 0:
        print(" Sa surid. Sundöö sai sulle saatuslikuks.")
    else:
        print(" Sa elasid Sundöö üle! Tubli töö!")

if __name__ == "__main__":
    print(" Tere tulemast mängu: SUNDÖÖ – Ela 12 tundi!")
    game_loop()
