import os
import sys
import json
import logging
from Src.Models.Enums import Weather
import random

class AppConfig:
    def __init__(self):
        self.conf = self.get_app_settings()
        self.greenHouseConfig = self.conf["GreenHouse"]
        self.testerConfig = self.greenHouseConfig["Tester"]
        self.greenHouseControllerConfig = self.greenHouseConfig["GreenHouseController"]

    def get_app_settings(self):
        """
           Reading the appSettings file.
        """
        try:
            ret = None
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            appsettings_path_base = os.path.join(base_path, "appsettings.json")
            if os.path.isfile(appsettings_path_base):
                with open(appsettings_path_base) as f:
                    ret = json.load(f)
            return ret
        except FileNotFoundError:
            logging.error(f"Config: appsettings not found")
        except BaseException as err:
            logging.error("Config: Error get_app_settings - {0}".format(err))

    def init_logger(self):
        """
            Initialization of the project's logger.
        """
        try:
            basePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            logger_folder = os.path.join(basePath, self.conf["GreenHouse"]["LoggingFilePath"])
            file_handler = logging.FileHandler(filename=os.path.join(logger_folder, 'logger.txt'),
                                               mode='a')
            stdout_handler = logging.StreamHandler(stream=sys.stdout)
            handlers = [file_handler, stdout_handler]
            logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG,
                                handlers=handlers)
            logging.debug('initializing')
        except FileNotFoundError:
            logging.error(f"Config: init_logger not found logger")
        except BaseException as err:
            logging.error("Config: Error init_logger - {0}".format(err))

    def water_and_light_exposure_by_weather(self) -> tuple:
        """
            The function randomly receives the weather and turns to appSettings.json.
            :return: receive the amount of water and light required for the selected random weather
            :rtype: tuple
        """
        weather = random.choice(list(Weather))
        light_exposure_weather = self.greenHouseControllerConfig["lightExposure"][weather.name]
        water = light_exposure_weather["Water"]
        intensity = light_exposure_weather["Intensity"]
        return intensity, water
