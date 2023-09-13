import datetime
import random
from Src.UnitTests.UnitTestBase import UnitTestBase
import logging


class PlantTester(UnitTestBase):
    def __init__(self):
        super().__init__()

    def run(self):
        """
        The function receives the desired number of days for testing.
        and calculates the growth of the plant according to the entered parameters.
        """
        try:
            print("----- Plant Tester -----")
            for day in range(self.max_days + 1):
                intensity, water = self.conf.water_and_light_exposure_by_weather()
                for plant in self.plants:
                    plant.water(amount=water)
                    plant.provide_light(intensity=intensity)
                    planet_growth = plant.grow()
                    print(f"{plant.name}: Day - {day}, Planet Growth - {round(planet_growth, 5)}, "
                          f"Height - {round(plant.height, 5)}")

        except BaseException as err:
            logging.error(f"PlantTester: Error run - {err}")

# If you want to run the tester independently
# if __name__ == '__main__':
#     try:
#         plantTester = PlantTester()
#         plantTester.run()
#     except Exception as err:
#         exit(1)
