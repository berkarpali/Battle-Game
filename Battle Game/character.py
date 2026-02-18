import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def attack(self, other):
        if self.is_alive():

            min_damage = max(0, self.attack_power - 5)
            max_damage = self.attack_power + 5
            damage = random.randint(min_damage, max_damage)

            if damage > 0 and random.random() < 0.2:
                damage *= 2
                print("CRITICAL HIT!!!")

            print(self.name, "dealt", damage, "damage")
            other.take_damage(damage)

        else:
            print(self.name, "is dead and can not attack")

    def show_status(self):
        print(self.name, "Health:", self.health)

