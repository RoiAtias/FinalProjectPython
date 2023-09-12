from enum import Enum


class Weather(Enum):
    Clear_Sky = 1
    Partly_Cloudy = 2
    Cloudy = 3
    Rainy = 4


class Menu(Enum):
    Run = 1
    Tester = 2
    Read_Me = 3
    Exit = 4


class Tester(Enum):
    Plant = 1
    Irrigation_System = 2
    Green_House_Controller = 3
    Back_To_Menu = 4


class ReturnMenu(Enum):
    Main_Menu = 1
    Exit = 2
