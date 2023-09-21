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
        self.conf = AppConfig()
        self.irrigation_system = IrrigationSystem(self.conf.greenHouseControllerConfig["WaterLevelIrrigationSystem"])

    def add_plant(self, plant: Plant):
        """
        This function takes a plant and adds it to the existing array of plants.

        :param plant: A plant object
        :type plant: Plant
        """
        try:
            if self.plants:
                self.plants.append(plant)
        except Exception as e:
            print(f"GreenhouseController: Error Add_plant adding element: {e}")
            logging.error(f"GreenhouseController: Error Add_plant adding element: {e}")

    def water_plants(self):
        """
          This function calls the irrigation system to water the plants according to the amount of
          water required for each plant.
        """
        if len(self.plants) > 0:
            self.irrigation_system.irrigate_plants(self.plants)
        else:
            print(
                f"GreenhouseController: Error water_plants The number of plants in the list is less than or equal to 0")

    def run_simulation(self, days: int):
        """
        This function randomly receives the amount of light and the amount of water and, depending on the number of
        days,activates the irrigation system. and goes over a plant separately and subtracts the required amount.

        :param days: The desired number of days to lift the simulation
        :type days: int
        """
        try:
            if days > 0:
                water_level_irrigation_system = self.conf.greenHouseControllerConfig["WaterLevelIrrigationSystem"]
                intensity = self.conf.light_exposure_by_weather()
                if intensity > 0 and water_level_irrigation_system > 0:
                    water_counter = self.irrigation_system.water_level
                    for day in range(days + 1):
                        if sum(plant.water_requirement for plant in self.plants) < self.irrigation_system.water_level:
                            self.water_plants()
                            self.execute_process_plant(day, intensity, self.irrigation_system.water_level)
                        else:
                            print("There is not enough water in the irrigation system")
                            break
                else:
                    print(f"GreenhouseController: Error run_simulation  Error The amount of light or water is not "
                          f"greater than 0")
            else:
                print("Error The number of days should be a positive number")
        except BaseException as err:
            print(f"GreenhouseController: Error run_simulation - {err}")
            logging.error(f"GreenhouseController: Error run_simulation - {err}")

    def execute_process_plant(self, day: int, intensity: float, water_counter: float):
        """
        The function receives a list of plants and handles the growth of each plant separately.

        :param day: day number in the run is used for printing.
        :type day: int
        :param intensity: amount of light
        :type intensity: float
        :param water_counter: amount of water in the irrigation system
        :type water_counter: float
        """
        try:
            for plant in self.plants:
                water_counter -= plant.water_requirement
                plant.provide_light(intensity)
                plant_growth = plant.grow()
                print(f"Plant {plant.name} : Day - {day}, Height - {round(plant.height, 5)}, "
                      f"Plant Growth - {round(plant_growth, 5)}, Water In Irrigation system - {water_counter}")
        except BaseException as err:
            print(f"GreenhouseController: Error execute_process - {err}")
            logging.error(f"GreenhouseController: Error execute_process - {err}")
