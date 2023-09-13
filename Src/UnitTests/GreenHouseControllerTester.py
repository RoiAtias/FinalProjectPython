from Src.Entites.GreenHouseController import GreenHouseController
import logging
from Src.UnitTests.UnitTestBase import UnitTestBase


class GreenHouseControllerTester(UnitTestBase):
    def __init__(self):
        super().__init__()
        self.green_house_controller = GreenHouseController()

    def run(self):
        """
        This function performs a run of run_simulation after adding the water in the irrigation system.
        """
        try:
            print("----- Green House Controller Tester -----")
            self.green_house_controller.irrigation_system.add_water(self.water_level_irrigation_system)
            self.green_house_controller.run_simulation(self.number_days_system_run)

        except BaseException as err:
            print(f"GreenHouseControllerTester: Error run - {err}")
            logging.error(f"GreenHouseControllerTester: Error run - {err}")

# If you want to run the tester independently
# if __name__ == '__main__':
#     try:
#         greenHouseControllerTester = GreenHouseControllerTester()
#         greenHouseControllerTester.run()
#     except Exception as err:
#         exit(1)
