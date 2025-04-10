class Resource:
    def __init__(self, resource_type, quantity):
        self.resource_type = resource_type  # Ressursi tüüp (nt vesi, toit)
        self.quantity = quantity  # Ressursi kogus

    def __repr__(self):
        return f"{self.resource_type}: {self.quantity}"


class Platform:
    def __init__(self, level_number, resources):
        self.level_number = level_number  # Tasandi number
        self.resources = resources  # Ressursid, mis on sellel tasandil saadaval

    def move_resources(self, next_level, resource_to_move, quantity):
        """
        Liigutab ressursse järgmisele tasandile.
        :param next_level: Järgmine tasand, kuhu ressursid liiguvad
        :param resource_to_move: Ressurss, mida liigutatakse
        :param quantity: Kogus, mis liigutatakse
        """
        if resource_to_move.resource_type in self.resources:
            if self.resources[resource_to_move.resource_type] >= quantity:
                # Ressursi liikumine
                self.resources[resource_to_move.resource_type] -= quantity
                # Kui ressurss ei ole juba järgmise taseme jaoks loodud, siis lisatakse see
                if resource_to_move.resource_type not in next_level.resources:
                    next_level.resources[resource_to_move.resource_type] = 0
                next_level.resources[resource_to_move.resource_type] += quantity
                print(f"Liigutatud {quantity} {resource_to_move.resource_type} tasandile {next_level.level_number}")
            else:
                print(f"Ei piisa {resource_to_move.resource_type} liikumiseks.")
        else:
            print(f"Ressurssi {resource_to_move.resource_type} ei leitud sellel tasandil.")

    def __repr__(self):
        return f"Tasand {self.level_number}, Ressursid: {self.resources}"


# Testimine:
if __name__ == "__main__":
    # Loome ressursid
    water = Resource("Water", 100)
    food = Resource("Food", 50)

    # Loome kaks tasandit
    level_1 = Platform(1, {"Water": 100, "Food": 50})
    level_2 = Platform(2, {})

    # Prindime algandmed
    print(level_1)
    print(level_2)

    # Liigutame ressursse tasandilt 1 tasandile 2
    level_1.move_resources(level_2, water, 30)
    level_1.move_resources(level_2, food, 20)

    # Prindime andmed pärast liikumist
    print(level_1)
    print(level_2)
