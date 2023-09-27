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
        """
          The function adds an amount of water to the plant.

          :param amount: amount of water
          :type amount: float
        """

        try:
            if amount > 0:
                self.water_level += amount
            else:
                print(f"Error it is not possible to add a negative amount of water to the plant")
        except Exception as e:
            print(f"Plant: Error water Added amount: {e}")
            logging.error(f"Plant: Error water Added amount: {e}")

    def provide_light(self, intensity: float):
        """
          The function adds the amount of light to the plant.

          :param intensity: amount of light
          :type intensity: float
        """

        try:
            if intensity > 0:
                self.light_exposure = intensity
            else:
                print("Error The amount of light the function can receive must be greater than 0")
        except Exception as e:
            print(f"Plant: Error provide_light Added intensity: {e}")
            logging.error(f"Plant: Error provide_light Added intensity: {e}")

    def grow(self) -> float:
        """
           The function calculates the growth of the plant and if there is not enough light or water the plant does not
           grow.The function then increments the size of the plant and its age.
           And finally resets the amount of water of the plant

           :return: The function returns the growth parameter of the plant
           :rtype: float
        """
        try:
            planet_growth = random.uniform(0, 1) * min(self.water_level - self.water_requirement,
                                                       1)  # There is enough light and water

            if self.light_exposure < self.light_requirement:  # Checking whether there is enough light
                planet_growth = 0

            if self.height + planet_growth < 0:
                # Check state of wilting of the plant, the height cannot be at a negative height
                print(f"The plant {self.name} is dead")
                self.height = 0
            else:
                self.height += planet_growth

            self.age += 1
            self.water_level = 0

            return planet_growth

        except BaseException as err:
            print(f"Plant: Error grow - {err}")
            logging.error(f"Plant: Error grow - {err}")

    def get_random_number_by_date(self) -> float:
        """
           The function calculates a random number between 0-1 that changes every day only.

           :return: A random number between 0-1
           :rtype: float
        """
        random.seed(datetime.date.today())
        return random.uniform(0, 1)
