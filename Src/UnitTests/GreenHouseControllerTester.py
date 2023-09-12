from Src.Entites.FileUtils import FileUtils
from Src.Entites.GreenHouseController import GreenHouseController
import logging
from Src.UnitTests.UnitTestBase import UnitTestBase


class GreenHouseControllerTester(UnitTestBase):
    def __init__(self):
        super().__init__()
        self.green_house_controller = GreenHouseController()

    def run(self):
        try:
            print("----- Green House Controller Tester -----")
            self.green_house_controller.irrigation_system.add_water(310)
            self.green_house_controller.run_simulation(self.max_days)

        except BaseException as err:
            logging.error(f"GreenHouseControllerTester: Error run - {err}")


# if __name__ == '__main__':
#     try:
#         greenHouseControllerTester = GreenHouseControllerTester()
#         greenHouseControllerTester.run()
#     except Exception as err:
#         exit(1)
