import datetime
import random
import logging


class Plant:
    def __init__(self, name: str, species: str, age: int, water_level: float, water_requirement: float,
                 light_requirement: float, height: float):
        self.name = name
        self.species = species
        self.age = age
        self.water_level = water_level
        self.light_exposure = self.get_random_number_by_date()
        self.water_requirement = water_requirement
        self.light_requirement = light_requirement
        self.height = height

    def water(self, amount: float):
        self.water_level += amount

    def provide_light(self, intensity: float):
        self.light_exposure = intensity

    def grow(self):
        try:
            planet_growth = random.uniform(0, 1) * min(self.water_level - self.water_requirement,
                                                       1)  # There is enough light and water

            if self.light_exposure < self.light_requirement:  # Checking whether there is enough light
                planet_growth = 0

            self.height += planet_growth
            self.age += 1
            self.water_level = 0

            return planet_growth

        except BaseException as err:
            logging.error(f"Plant: Error grow - {err}")

    def get_random_number_by_date(self):
        random.seed(datetime.date.today())
        return random.uniform(0, 1)
