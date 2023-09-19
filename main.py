from Src.Entites.GreenHouseController import GreenHouseController
from Src.Models.Enums import Tester
from Src.Models.Enums import ReturnMenu
from Src.Models.Enums import Menu
from Src.Shared.FileUtils import FileUtils
from Src.UnitTests.PlantTester import PlantTester
from Src.UnitTests.GreenHouseControllerTester import GreenHouseControllerTester
from Src.UnitTests.IrrigationSystemTester import IrrigationSystemTester
from Src.Shared.AppConfig import AppConfig
import sys
import logging


class Main:
    def __init__(self):
        self.green_house_controller = GreenHouseController()
        self.file_utils = FileUtils()
        self.config = AppConfig()
        self.logger = self.config.init_logger()

    def run(self):
        selected_choice = self.main_menu()
        self.run_main_menu(selected_choice)
        return_selected_choice = self.return_main_menu()
        self.run_return_menu(return_selected_choice)

    def main_menu(self):
        print("")
        print("Hello! Welcome to GreenHouse!")
        print("Please select the choice from the following options : ")
        print("1. Run Simulation")
        print("2. Testers")
        print("3. Introductions")
        print("4. Exit")
        selected_choice = input("choice: ")
        if self.check_valid_input_number(selected_choice):
            return int(selected_choice)
        else:
            self.main_menu()

    def sub_menu_tester(self):
        print("")
        print("Tester Menu")
        print("Please select the choice from the following options : ")
        print("1. Plant")
        print("2. Irrigation System")
        print("3. Green House Controller")
        print("4. Back Main Menu")
        selected_choice = input("choice: ")
        if self.check_valid_input_number(selected_choice):
            return int(selected_choice)
        else:
            self.sub_menu_tester()

    def return_main_menu(self):
        print("")
        print("Please select the choice from the following options : ")
        print("1. Main Menu")
        print("2. Exit")
        selected_choice = input("choice: ")
        if self.check_valid_input_number(selected_choice):
            return int(selected_choice)
        else:
            self.return_main_menu()

    def run_main_menu(self, selected_choice: int):
        if selected_choice == Menu.Run.value:
            print("----- GreenHouseController - Run simulation -----")
            self.green_house_controller.run_simulation(self.config.greenHouseConfig["NumberDaysSystemRun"])
        elif selected_choice == Menu.Tester.value:
            selected_seb_menu_tester = self.sub_menu_tester()
            self.run_sub_menu(selected_choice=selected_seb_menu_tester)
        elif selected_choice == Menu.Read_Me.value:
            print(self.file_utils.get_read_me_file())
        elif selected_choice == Menu.Exit.value:
            sys.exit()
        else:
            print(f"Choice {selected_choice} is incorrect, please choose again")
            self.run()

    def run_sub_menu(self, selected_choice: int):
        if selected_choice == Tester.Plant.value:
            print("----- Plant Tester -----")
            plant = PlantTester()
            plant.run()
        elif selected_choice == Tester.Irrigation_System.value:
            print("----- Irrigation System Tester -----")
            irrigation_system = IrrigationSystemTester()
            irrigation_system.run()
        elif selected_choice == Tester.Green_House_Controller.value:
            print("----- Green House Controller Tester -----")
            green_house_controller = GreenHouseControllerTester()
            green_house_controller.run()
        elif selected_choice == Tester.Back_To_Menu.value:
            self.run()
        else:
            print(f"Choice {selected_choice} is incorrect, please choose again")
            self.run()

    def run_return_menu(self, selected_choice: int):
        if selected_choice == ReturnMenu.Main_Menu.value:
            self.run()
        elif selected_choice == ReturnMenu.Exit.value:
            sys.exit()
        else:
            print(f"Choice {selected_choice} is incorrect, please choose again")
            self.run()

    def check_valid_input_number(self, selected_choice):
        is_valid = True
        if not selected_choice.isdigit():
            print(f"Choice {selected_choice} is incorrect, please choose again")
            is_valid = False
        return is_valid


if __name__ == '__main__':
    try:
        main = Main()
        main.run()
    except Exception as err:
        logging.error(f"Main: Error main - {err}")
        exit(1)
