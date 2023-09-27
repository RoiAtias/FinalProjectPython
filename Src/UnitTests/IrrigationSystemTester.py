from Src.Entites.IrrigationSystem import IrrigationSystem
import logging
from Src.UnitTests.UnitTestBase import UnitTestBase


class IrrigationSystemTester(UnitTestBase):
    def __init__(self):
        super().__init__()

    def run(self):
        """
            This function activates the irrigation system according to the number of days set for it.
            and checks in each iteration whether there is enough water in the irrigation system and if not, it stops.
        """
        try:
            if self.water_level_irrigation_system > 0 and self.number_days_system_run >= 0:
                self.irrigation_system = IrrigationSystem(water_level=self.water_level_irrigation_system)
                water_counter = self.irrigation_system.water_level
                for day in range(self.number_days_system_run):
                    intensity = self.conf.light_exposure_by_weather()

                    self.irrigation_system.irrigate_plants(self.plants)
                    for plant in self.plants:
                        plant.provide_light(intensity)
                        planet_growth = plant.grow()
                        if water_counter - plant.water_requirement > 0:
                            water_counter = water_counter - plant.water_requirement
                        print(f"{plant.name} : Day - {day}, Water in Irrigation System - {round(water_counter, 5)}, "
                              f"Planet Growth - {round(planet_growth, 5)}, "
                              f"Height - {round(plant.height, 5)}")

        except BaseException as err:
            print(f"IrrigationSystemTester: Error run_simulation - {err}")
            logging.error(f"IrrigationSystemTester: Error run_simulation - {err}")

# If you want to run the tester independently
# if __name__ == '__main__':
#     try:
#         irrigationSystemTester = IrrigationSystemTester()
#         irrigationSystemTester.run()
#     except Exception as err:
#         exit(1)
