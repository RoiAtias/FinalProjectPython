import datetime
import random
from Src.UnitTests.UnitTestBase import UnitTestBase
import logging


class PlantTester(UnitTestBase):
    def __init__(self):
        super().__init__()

    def run(self):
        """
        This function receives the desired number of days for testing.
        and calculates the growth of the plant according to the entered parameters.
        """
        try:
            if self.number_days_system_run >= 0 and self.conf.testerConfig["WaterPlant"] > 0:
                for day in range(self.number_days_system_run + 1):
                    intensity = self.conf.light_exposure_by_weather()
                    for plant in self.plants:
                        plant.water(amount=self.conf.testerConfig["WaterPlant"])
                        plant.provide_light(intensity=intensity)
                        planet_growth = plant.grow()
                        print(f"{plant.name}: Day - {day}, Planet Growth - {round(planet_growth, 5)}, "
                              f"Height - {round(plant.height, 5)}")
        except BaseException as err:
            print(f"PlantTester: Error run - {err}")
            logging.error(f"PlantTester: Error run - {err}")

# If you want to run the tester independently
# if __name__ == '__main__':
#     try:
#         plantTester = PlantTester()
#         plantTester.run()
#     except Exception as err:
#         exit(1)
