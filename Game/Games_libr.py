from abc import ABC, abstractmethod
import random

class Warship(ABC):
    health = None
    speed = None
    location = None
    armor = None

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def take_damage(self):
        pass


class Weapon(ABC):
    damage = None
    accuracy = None
    firing_range = None
    rate_of_fire = None
    critical_hit_chance = None



class Coordinates():
    x = None
    y = None

    def __init__(self, init_x, init_y):
        self.crd_x = init_x
        self.crd_y = init_y

    @property
    def crd_x(self):
        return self.x

    @crd_x.setter
    def crd_x(self, init_x):
        if not isinstance(init_x, (str, float)):
            raise TypeError
        else:
            self.x = init_x

    @property
    def crd_y(self):
        return self.y

    @crd_y.setter
    def crd_y(self, init_y):
        if not isinstance(init_y, (str, float)):
            raise TypeError
        else:
            self.y = init_y


class Lincore(Warship):

    missile_defense_points = None

    def __init__(self, init_health, init_speed, init_location, init_armor, init_missile_defense_points):
        self.health_point = init_health
        self.ship_speed = init_speed
        self.location_coordinates = init_location
        self.armor_point = init_armor
        self.missile_defense_chance = init_missile_defense_points

    @property
    def health_point(self):
        return self.health

    @health_point.setter
    def health_point(self,init_health):
        if not isinstance(init_health, (int, float)):
            raise TypeError
        else:
            self.health = init_health

    @property
    def ship_speed(self):
        return self.speed

    @ship_speed.setter
    def ship_speed(self, init_speed):
        if not isinstance(init_speed, (int, float)):
            raise TypeError
        else:
            self.speed = init_speed

    @property
    def location_coordinates(self):
        return self.location

    @location_coordinates.setter
    def location_coordinates(self, init_location):
        if not isinstance(init_location, Coordinates):
            raise TypeError
        else:
            self.location = init_location

    @property
    def missile_defense_chance(self):
        return self.missile_defense_points

    @missile_defense_chance.setter
    def missile_defense_chance(self,init_missile_defense_points):
        if not isinstance(init_missile_defense_points, str):
            raise TypeError
        else: self.missile_defense_points = init_missile_defense_points


    def missile_defence(self):
        status_missile_defence = False
        chanse_counter = random.randrange(0, 100)

        if chanse_counter < self.missile_defense_points:
            status_missile_defence = True
        return status_missile_defence

    def take_damage(self, final_damage_dealt):
        if random.randrange(0, 100)


class MissileCrusier(Warship):
    missile_defense_points = None

    def __init__(self, init_health, init_speed, init_location, init_armor, init_missile_defense_points):
        self.health_point = init_health
        self.ship_speed = init_speed
        self.location_coordinates = init_location
        self.armor_point = init_armor
        self.missile_defense_chance = init_missile_defense_points

    @property
    def health_point(self):
        return self.health

    @health_point.setter
    def health_point(self, init_health):
        if not isinstance(init_health, (int, float)):
            raise TypeError
        else:
            self.health = init_health

    @property
    def ship_speed(self):
        return self.speed

    @ship_speed.setter
    def ship_speed(self, init_speed):
        if not isinstance(init_speed, (int, float)):
            raise TypeError
        else:
            self.speed = init_speed

    @property
    def location_coordinates(self):
        return self.location

    @location_coordinates.setter
    def location_coordinates(self, init_location):
        if not isinstance(init_location, Coordinates):
            raise TypeError
        else:
            self.location = init_location

    @property
    def missile_defense_chance(self):
        return self.missile_defense_points

    @missile_defense_chance.setter
    def missile_defense_chance(self, init_missile_defense_points):
        if not isinstance(init_missile_defense_points, str):
            raise TypeError
        else:
            self.missile_defense_points = init_missile_defense_points

    def missile_defence(self):
        status_missile_defence = False
        chanse_counter = random.randrange(0, 100)

        if chanse_counter < self.missile_defense_points:
            status_missile_defence = True
        return status_missile_defence


class TorpedoDestroyer(Warship):

    def __init__(self, init_health, init_speed, init_location, init_armor):
        self.health_point = init_health
        self.ship_speed = init_speed
        self.location_coordinates = init_location
        self.armor_point = init_armor

    @property
    def health_point(self):
        return self.health

    @health_point.setter
    def health_point(self, init_health):
        if not isinstance(init_health, (int, float)):
            raise TypeError
        else:
            self.health = init_health

    @property
    def ship_speed(self):
        return self.speed

    @ship_speed.setter
    def ship_speed(self, init_speed):
        if not isinstance(init_speed, (int, float)):
            raise TypeError
        else:
            self.speed = init_speed

    @property
    def location_coordinates(self):
        return self.location

    @location_coordinates.setter
    def location_coordinates(self, init_location):
        if not isinstance(init_location, Coordinates):
            raise TypeError
        else:
            self.location = init_location


class Corvette(Warship):

    def __init__(self, init_health, init_speed, init_location, init_armor):
        self.health_point = init_health
        self.ship_speed = init_speed
        self.location_coordinates = init_location
        self.armor_point = init_armor

    @property
    def health_point(self):
        return self.health

    @health_point.setter
    def health_point(self, init_health):
        if not isinstance(init_health, (int, float)):
            raise TypeError
        else:
            self.health = init_health

    @property
    def ship_speed(self):
        return self.speed

    @ship_speed.setter
    def ship_speed(self, init_speed):
        if not isinstance(init_speed, (int, float)):
            raise TypeError
        else:
            self.speed = init_speed

    @property
    def location_coordinates(self):
        return self.location

    @location_coordinates.setter
    def location_coordinates(self, init_location):
        if not isinstance(init_location, Coordinates):
            raise TypeError
        else:
            self.location = init_location


class HeavyShipGan(Weapon):

    def __init__(self, init_damage, init_accuracy, init_firing_range, init_rate_of_fire, init_critical_hit_chance):
        self.damage_point = init_damage
        self.accuracy_point = init_accuracy
        self.firing_range_max = init_firing_range
        self.rate_of_fire_max = init_rate_of_fire
        self.critical_hit_point = init_critical_hit_chance

    @property
    def damage_point(self):
        return self.damage

    @damage_point.setter
    def damage_point(self,init_damage):
        if not isinstance(init_damage, (int, float)):
            raise TypeError

    @property
    def accuracy_point(self):
        return self.accuracy

    @accuracy_point.setter
    def accuracy_point(self, init_accuracy):
        if not isinstance(init_accuracy, (int, float)):
            raise TypeError

    @property
    def firing_range_max(self):
        return self.firing_range

    @firing_range_max.setter
    def firing_range_max(self, init_firing_range):
        if not isinstance(init_firing_range, (int, float)):
            raise TypeError

    @property
    def rate_of_fire_max(self):
        return self.rate_of_fire

    @rate_of_fire_max.setter
    def rate_of_fire_max(self, init_rate_of_fire):
        if not isinstance(init_rate_of_fire, (int, float)):
            raise TypeError

    @property
    def critical_hit_point(self):
        return self.critical_hit_chance

    @critical_hit_point.setter
    def critical_hit_point(self, init_critical_hit_chance):
        if not isinstance(init_critical_hit_chance, (int, float)):
            raise TypeError

    def fire(self, target):
        final_damage_dealt = 0

        if not isinstance(target, Warship):
            raise TypeError

        for shot in range(self.rate_of_fire):
            if random.randrange(0, 100) <= self.accuracy:
                if random.randrange(0, 100) <= target.
                shot_damage = self.damage
                if random.randrange(0, 100) <= self.critical_hit_chance:
                    shot_damage = shot_damage * 2
                final_damage_dealt = final_damage_dealt + shot_damage

        return final_damage_dealt


