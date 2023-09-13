from Src.SharedLogic.AppConfig import AppConfig
from Src.SharedLogic.FileUtils import FileUtils
from Src.Models.Enums import Tester

class UnitTestBase:
    def __init__(self):
        self.fileUtils = FileUtils()
        self.plants = []
        self.conf = AppConfig()
        self.irrigation_system = None
        self.max_days = self.conf.greenHouseConfig["MaxDays"]
        self.plants = self.fileUtils.get_plants()
        self.water_level_irrigation_system = self.conf.testerConfig["water_level_irrigation_system"]

    def run(self):
        pass
