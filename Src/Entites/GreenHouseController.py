import random
import logging
from Src.Entites.Plant import Plant
from Src.Entites.IrrigationSystem import IrrigationSystem
from Src.Entites.FileUtils import FileUtils
from Src.Entites.Config import Config
from Src.Models.Enums import Weather

class GreenHouseController:
    def __init__(self):
        self.fileUtils = FileUtils()
        self.plants = self.fileUtils.get_plants()
        self.irrigation_system = IrrigationSystem()
        self.conf = Config()

    def add_plant(self, plant: Plant):
     self.plants.append(plant)

    def water_plants(self):
        self.irrigation_system.irrigate_plants(self.plants)

    def run_simulation(self, days):
        try:
            print("----- GreenHouseController - Run simulation -----")
            intensity, water = self.water_and_light_exposure_by_weather(random.choice(list(Weather)))
            water_counter = self.irrigation_system.water_level

            for day in range(days + 1):
                if (self.irrigation_system.check_water_level_in_irrigation_system(self.plants)):
                    self.water_plants()
                    for plant in self.plants:
                       water_counter -= plant.water_requirement
                       self.execute_process(plant,day, water, intensity, water_counter)
                else:
                    print("There is not enough water in the irrigation system")
                    break

        except BaseException as err:
            logging.error(f"GreenhouseController: Error run_simulation - {err}")

    def execute_process(self, plant: Plant, day: int, water: float, intensity: float, water_counter: float):
        try:
            plant.water(water)
            plant.provide_light(intensity)
            plant_growth = plant.grow()
            print(f"Plant {plant.name} : Day {day}, height - {round(plant.height, 5)} , "
                  f"plant_growth - {round(plant_growth, 5)} , water_in_irrigation_system - {water_counter}")
        except BaseException as err:
            logging.error(f"GreenhouseController: Error execute_process - {err}")

    def water_and_light_exposure_by_weather(self, weather: Weather):
        light_exposure_weather = self.conf.greenHouseControllerConfig["lightExposure"][weather.name]
        water = light_exposure_weather["Water"]
        intensity = light_exposure_weather["Intensity"]
        return intensity, water



