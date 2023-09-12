from Src.Entites.Plant import Plant
from Src.Entites.Config import Config
from Src.Entites.FileUtils import FileUtils

class UnitTestBase:
    def __init__(self):
        self.fileUtils = FileUtils()
        self.plants = []
        self.conf = Config()
        self.irrigation_system = None
        self.max_days = self.conf.greenHouseConfig["MaxDays"]
        self.plants = self.fileUtils.get_plants()

    def run(self):
        pass