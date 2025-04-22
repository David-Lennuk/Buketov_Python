import random
import time

class Resource:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Food(Resource):
    def __init__(self, name, value, food_points, hp_points, expose_time):
        super().__init__(name, value)
        self.food_points = food_points
        self.hp_points = hp_points
        self.expose_time = expose_time  # Toidu säilivusaeg

    def update(self):
        """Aja jooksul toidu kvaliteedi vähenemine"""
        if self.expose_time > 0:
            self.expose_time -= 1
        else:
            self.food_points = 0
            self.hp_points = 0

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, resource):
        self.items.append(resource)

    def remove(self, resource):
        self.items.remove(resource)

    def find_resource(self, resource_name):
        for item in self.items:
            if item.name == resource_name:
                return item
        return None

class Player:
    def __init__(self, max_hp, max_energy, max_food, inventory):
        self.max_hp = max_hp
        self.max_energy = max_energy
        self.max_food = max_food
        self.hp = max_hp
        self.energy = max_energy
        self.food = max_food
        self.inventory = inventory

    def get_hp(self):
        return self.hp

    def set_hp(self, value):
        self.hp = value

    def get_energy(self):
        return self.energy

    def set_energy(self, value):
        self.energy = value

    def get_food(self):
        return self.food

    def set_food(self, value):
        self.food = value

class FoodEarning:
    def __init__(self, food):
        self.food = food

    def affect_player(self, player):
        player.set_hp(player.get_hp() + self.food.hp_points)
        player.set_energy(player.get_energy() + self.food.food_points)

class Night:
    def __init__(self, game):
        self.game = game

    def update(self):
        """Öö jooksul igal ajaintervallil täiendatakse mängija seisundit."""
        self.game.tick()

class Game:
    def __init__(self, player):
        self.player = player
        self.time = 12  # Mängu aeg
        self.time_tick = 1  # Ajastiku samm
        self.night = Night(self)

    def tick(self):
        """Aeg möödub, ressursside ja toidu vananemine"""
        for item in self.player.inventory.items:
            if isinstance(item, Food):
                item.update()

        self.time -= self.time_tick
        if self.time <= 0 or self.player.get_hp() <= 0:
            self.end_game()

    def end_game(self):
        if self.player.get_hp() <= 0:
            print("Sa surid.")
        else:
            print("Aeg sai otsa. Mäng on lõppenud.")
        exit()

    def main(self):
        while self.time > 0 and self.player.get_hp() > 0:
            print(f"\nAeg: {self.time} tundi jäänud")
            print(f"Tervis: {self.player.get_hp()}")
            print(f"Energia: {self.player.get_energy()}")
            print(f"Toidukogus: {self.player.get_food()}")
            print("\nValikud:")
            print("1. Puhka")
            print("2. Liigu edasi")
            print("3. Riskige")
            print("4. Otsi toitu")
            choice = input("Vali tegevus (1-4): ")

            if choice == "1":
                self.rest()
            elif choice == "2":
                self.move()
            elif choice == "3":
                self.risk()
            elif choice == "4":
                self.find_food()
            else:
                print("Vigane valik!")

            self.night.update()

    def rest(self):
        if self.player.get_food() > 0:
            self.player.set_energy(self.player.get_energy() + 20)
            self.player.set_hp(self.player.get_hp() + 10)
            self.player.set_food(self.player.get_food() - 1)
            print("Puhkasid ja sõid veidi toitu.")
        else:
            print("Sul pole piisavalt toitu!")

    def move(self):
        if self.player.get_energy() > 30:
            self.player.set_energy(self.player.get_energy() - 30)
            self.player.set_food(self.player.get_food() - 1)
            self.player.set_hp(self.player.get_hp() - 10)
            print("Liikusite edasi...")
        else:
            print("Sul pole piisavalt energiat! Kaotasid tervist.")

    def risk(self):
        if random.choice([True, False]):
            print("Õnnestus! Sa leidsid toitu.")
            food = Food("Õnnelik toit", 1, 20, 10, 5)
            self.player.inventory.add(food)
        else:
            print("Oht! Sa said viga.")
            self.player.set_hp(self.player.get_hp() - 20)

    def find_food(self):
        food = Food("Leitud toit", 1, 15, 5, 3)
        self.player.inventory.add(food)
        print("Leidsid toidu!")

if __name__ == "__main__":
    inventory = Inventory()
    player = Player(100, 100, 3, inventory)
    game = Game(player)
    game.main()
