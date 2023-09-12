import datetime
import random
from Src.UnitTests.UnitTestBase import UnitTestBase

class PlantTester(UnitTestBase):
    def __init__(self):
        super().__init__()

    def run(self):
        print("----- Plant Tester -----")
        for day in range(self.max_days + 1):
            for plant in self.plants:
                plant.water(amount=0.35)
                plant.provide_light(intensity=0.8)
                planet_growth = plant.grow()
                print(f"{plant.name}: Day - {day}, PLANET_GROWTH - {round(planet_growth, 5)} - HEIGHT - {round(plant.height, 5)}")
        return

    def random_number_current_day_week(self, date: datetime):
        random.seed(str(date))
        return random.uniform(0, 1)

