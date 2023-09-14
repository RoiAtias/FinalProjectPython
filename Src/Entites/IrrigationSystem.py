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
            self.water_level += amount
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
            if len(plants) > 0:
                amount_water_irrigation = 0

                if self.water_level > 0:
                    amount_water_irrigation = self.water_level / len(plants)
                else:
                    print(f"IrrigationSystem: Error irrigate_plants : amount of water is less than or equal to 0")

                for plant in plants:
                    plant.water(amount_water_irrigation)
                    self.water_level -= plant.water_requirement

        except BaseException as err:
            print(f"IrrigationSystem: Error irrigate_plants - {err}")
            logging.error(f"IrrigationSystem: Error irrigate_plants - {err}")

    def check_water_level_in_irrigation_system(self, plants: list[Plant]) -> bool:
        """
           The function checks whether there is enough water in the irrigation system in relation to the
           amount of water required by all the plants together.

           :param plants: list of Plant
           :type plants: list[Plant]
           :return: Returns if the amount is sufficient in the water tank in the irrigation system
           :rtype: bool
        """
        is_valid = True
        sum_water_requirement = sum(plant.water_requirement for plant in plants)
        if sum_water_requirement > self.water_level:
            is_valid = False
            logging.error(f"IrrigationSystem: Error check_water_level_in_irrigation_system - "
                          f"There is not enough water in the irrigation system")
        return is_valid
