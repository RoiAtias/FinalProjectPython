import logging

from Src.Entites.Plant import Plant


class IrrigationSystem:
    def __init__(self, water_level=0):
        self.water_level = water_level

    def add_water(self, amount: float):
        """
             This function takes a plant and adds it to the existing array of plants.

             :param amount: amount of water
             :type amount: float
        """
        try:
            if amount > 0:
                self.water_level += amount
            else:
                print("The amount of water that can be put in the tank must be a positive number")
        except Exception as e:
            print(f"IrrigationSystem: Error add_water Added amount: {e}")
            logging.error(f"IrrigationSystem: Error add_water Added amount: {e}")

    def irrigate_plants(self, plants: list[Plant]):
        """
           The function receives the list of plants that need to be watered in the irrigation system.
           The function checks if the water level is greater than 0, then the amount of water in the tank
           is divided by the number of plants.
           After that, for each plant I water and also subtract from the amount of water in the tank the amount of
           water required for each plant

           :param plants: list of plant
           :type plants: list[Plant]
        """
        try:
            if plants:
                amount_water_irrigation = self.water_level / len(plants)
                for plant in plants:
                    plant.water(amount_water_irrigation)
                    self.water_level -= plant.water_requirement

        except BaseException as err:
            print(f"IrrigationSystem: Error irrigate_plants - {err}")
            logging.error(f"IrrigationSystem: Error irrigate_plants - {err}")
