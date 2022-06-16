from abc import ABC, abstractmethod

class Warship(ABC):
    health = None
    speed = None
    location = None

   def run(self):
        pass

    def attack(self):
        pass

    def take_damage(self):
        pass
