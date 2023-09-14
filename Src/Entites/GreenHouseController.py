import random
import logging
from Src.Entites.Plant import Plant
from Src.Entites.IrrigationSystem import IrrigationSystem
from Src.Shared.FileUtils import FileUtils
from Src.Shared.AppConfig import AppConfig


class GreenHouseController:
    def __init__(self):
        self.fileUtils = FileUtils()
        self.plants = self.fileUtils.get_plants()
        self.irrigation_system = IrrigationSystem()
        self.conf = AppConfig()

    def add_plant(self, plant: Plant):
        """
        This function takes a plant and adds it to the existing array of plants.

        :param plant: A plant object
        :type plant: Plant
        """
        try:
            self.plants.append(plant)
        except Exception as e:
            print(f"GreenhouseController: Error Add_plant adding element: {e}")
            logging.error(f"GreenhouseController: Error Add_plant adding element: {e}")

    def water_plants(self):
        """
          This function calls the irrigation system to water the plants according to the amount of
          water required for each plant.
        """
        self.irrigation_system.irrigate_plants(self.plants)

    def run_simulation(self, days: int):
        """
        This function randomly receives the amount of light and the amount of water and, depending on the number of
        days,activates the irrigation system. and goes over a plant separately and subtracts the required amount.

        :param days: The desired number of days to lift the simulation
        :type days: int
        """
        try:
            print("----- GreenHouseController - Run simulation -----")
            intensity, water = self.conf.water_and_light_exposure_by_weather()
            water_counter = self.irrigation_system.water_level
            for day in range(days + 1):
                if self.irrigation_system.check_water_level_in_irrigation_system(self.plants):
                    self.water_plants()
                    for plant in self.plants:
                        water_counter -= plant.water_requirement
                        self.execute_process(plant, day, water, intensity, water_counter)
                else:
                    print("There is not enough water in the irrigation system")
                    break

        except BaseException as err:
            print(f"GreenhouseController: Error run_simulation - {err}")
            logging.error(f"GreenhouseController: Error run_simulation - {err}")

    def execute_process(self, plant: Plant, day: int, water: float, intensity: float, water_counter: float):
        """
        This function The function receives a plant and performs on it the actions of introducing an amount of
        water and receiving an amount of light and activates the function of growth that exists in the plant.

        :param plant: The plant object.
        :type plant: Plant
        :param day: day number in the run is used for printing.
        :type day: int
        :param water: amount of water for watering the plant
        :type water: float
        :param intensity: amount of light
        :type intensity: float
        :param water_counter: amount of water in the irrigation system
        :type water_counter: float
        """
        try:
            plant.water(water)
            plant.provide_light(intensity)
            plant_growth = plant.grow()
            print(f"Plant {plant.name} : Day {day}, Height - {round(plant.height, 5)}, "
                  f"Plant Growth - {round(plant_growth, 5)}, Water In Irrigation system - {water_counter}")
        except BaseException as err:
            print(f"GreenhouseController: Error execute_process - {err}")
            logging.error(f"GreenhouseController: Error execute_process - {err}")
