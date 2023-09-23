from Src.Shared.AppConfig import AppConfig
from Src.Shared.FileUtils import FileUtils


class UnitTestBase:
    def __init__(self):
        self.fileUtils = FileUtils()
        self.plants = []
        self.conf = AppConfig()
        self.irrigation_system = None
        self.number_days_system_run = self.conf.testerConfig["NumberDaysSystemRun"]
        self.plants = self.fileUtils.get_plants()
        self.water_level_irrigation_system = self.conf.greenHouseControllerConfig["WaterLevelIrrigationSystem"]

    def run(self):
        pass
