from Src.Entites.IrrigationSystem import IrrigationSystem
import logging
from Src.UnitTests.UnitTestBase import UnitTestBase


class IrrigationSystemTester(UnitTestBase):
    def __init__(self):
        super().__init__()

    def run(self):
        try:
            print("----- Irrigation System Tester -----")
            intensity, water = self.conf.water_and_light_exposure_by_weather()
            self.irrigation_system = IrrigationSystem(water_level=self.water_level_irrigation_system)
            water_counter = self.irrigation_system.water_level
            for day in range(self.max_days + 1):
                if self.irrigation_system.check_water_level_in_irrigation_system(self.plants):
                    self.irrigation_system.irrigate_plants(self.plants)
                    for plant in self.plants:
                        plant.provide_light(intensity)
                        planet_growth = plant.grow()
                        water_counter = water_counter - plant.water_requirement
                        print(
                            f"{plant.name} : Day - {day}, Water in Irrigation System  - {round(water_counter, 5)}, Planet Growth {round(planet_growth, 5)}, "
                            f"Height - {round(plant.height, 5)}")
                else:
                    print("There is not enough water in the irrigation system")
                    break

        except BaseException as err:
            logging.error(f"GreenhouseController: Error run_simulation - {err}")



# if __name__ == '__main__':
#     try:
#         main = IrrigationSystemTester()
#         main.run()
#     except Exception as err:
#         exit(1)
