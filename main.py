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
        self.file_utils = FileUtils()
        self.config = AppConfig()
        self.logger = self.config.init_logger()
        self.max_number_of_attempts = self.config.greenHouseConfig["MaxNumberOfAttempts"]

    def run(self):
        selected_choice = self.main_menu()
        self.run_main_menu(selected_choice)
        self.execute_run_return_menu()

    def main_menu(self):
        """
                          Creating a main menu of the application
        """
        number_of_attempts = 0
        while number_of_attempts < self.max_number_of_attempts:
            try:
                print("")
                print("Hello! Welcome to GreenHouse!")
                print("Please select the choice from the following options:")
                print("1. Run Simulation")
                print("2. Testers")
                print("3. Introductions")
                print("4. Exit")
                return int(input("choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                number_of_attempts += 1
                print(f"You have {self.max_number_of_attempts - number_of_attempts} attempts left")
        print("You tried to enter incorrect values several times. Try again with a new run of the system, thanks")
        self.exit_program()

    def sub_menu_tester(self):
        """
            Creation of a test menu of the application
        """
        number_of_attempts = 0
        while number_of_attempts < self.max_number_of_attempts:
            try:
                print("")
                print("Tester Menu")
                print("Please select the choice from the following options:")
                print("1. Plant")
                print("2. Irrigation System")
                print("3. Green House Controller")
                print("4. Back Main Menu")
                return int(input("choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                number_of_attempts += 1
                print(f"You have {self.max_number_of_attempts - number_of_attempts} attempts left")
        print("You tried to enter incorrect values several times. Try again with a new run of the system, thanks")
        self.exit_program()

    def return_main_menu(self):
        """
             Creating a back menu from the application activity
        """
        number_of_attempts = 0
        while number_of_attempts < self.max_number_of_attempts:
            try:
                print("")
                print("Please select the choice from the following options:")
                print("1. Main Menu")
                print("2. Exit")
                return int(input("choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                number_of_attempts += 1
                print(f"You have {self.max_number_of_attempts - number_of_attempts} attempts left")
        print("You tried to enter incorrect values several times. Try again with a new run of the system, thanks")
        self.exit_program()

    def run_main_menu(self, selected_choice: int):
        """
            The function runs the actions from the main menu
        """
        if selected_choice == Menu.Run.value:
            green_house_controller = GreenHouseController()
            print("")
            print("----- GreenHouseController - Run simulation -----")
            green_house_controller.run_simulation(self.config.greenHouseConfig["NumberDaysSystemRun"])
        elif selected_choice == Menu.Tester.value:
            self.execute_seb_menu_tester()
        elif selected_choice == Menu.Read_Me.value:
            print("")
            print("----- About -----")
            print(self.file_utils.get_read_me_file())
        elif selected_choice == Menu.Exit.value:
            self.exit_program()
        else:
            print(f"Choice {selected_choice} is incorrect, please choose again")
            self.run()

    def run_sub_menu(self, selected_choice: int):
        """
             The function runs the actions from the tests menu
        """
        if selected_choice == Tester.Plant.value:
            print("")
            print("----- Plant Tester -----")
            plant = PlantTester()
            plant.run()
        elif selected_choice == Tester.Irrigation_System.value:
            print("")
            print("----- Irrigation System Tester -----")
            irrigation_system = IrrigationSystemTester()
            irrigation_system.run()
        elif selected_choice == Tester.Green_House_Controller.value:
            print("")
            print("----- Green House Controller Tester -----")
            green_house_controller = GreenHouseControllerTester()
            green_house_controller.run()
        elif selected_choice == Tester.Back_To_Menu.value:
            self.run()
        else:
            print(f"Choice {selected_choice} is incorrect, please choose again")
            self.execute_seb_menu_tester()

    def run_return_menu(self, selected_choice: int):
        """
        The function displays a back menu from the list of actions
        """
        if selected_choice == ReturnMenu.Main_Menu.value:
            self.run()
        elif selected_choice == ReturnMenu.Exit.value:
            self.exit_program()
        else:
            print(f"Choice {selected_choice} is incorrect, please choose again")
            self.execute_run_return_menu()

    def execute_seb_menu_tester(self):
        """
        The function activates the menu of the system's testers
        """
        selected_seb_menu_tester = self.sub_menu_tester()
        self.run_sub_menu(selected_choice=selected_seb_menu_tester)

    def execute_run_return_menu(self):
        """
              The function activates the menu of return to the initial menu
        """
        return_selected_choice = self.return_main_menu()
        self.run_return_menu(return_selected_choice)

    def exit_program(self):
        """
              The function exits the program
        """
        sys.exit()


if __name__ == '__main__':
    try:
        main = Main()
        main.run()
    except Exception as err:
        logging.error(f"Main: Error main - {err}")
        exit(1)
