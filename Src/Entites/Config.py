import os
import sys
import json
import logging


class Config:
    def __init__(self):
        self.conf = self.get_app_settings()
        self.init_logger()
        self.greenHouseConfig = self.conf["GreenHouse"]
        self.greenHouseControllerConfig = self.conf["GreenHouse"]["GreenHouseController"]


    def get_app_settings(self):
        try:
            ret = None
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            appsettings_path_base = os.path.join(base_path,"appsettings.json")
            if os.path.isfile(appsettings_path_base):
                with open(appsettings_path_base) as f:
                    ret = json.load(f)
            return ret
        except FileNotFoundError:
            logging.error(f"Config: appsettings not found")
        except BaseException as err:
            logging.error("Config: Error get_app_settings - {0}".format(err))

    def init_logger(self):
        try:
            basePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            logger_folder = os.path.join(basePath, self.conf["GreenHouse"]["LoggingFilePath"])
            file_handler = logging.FileHandler(filename= os.path.join(logger_folder, 'logger.txt'),
                                               mode='a')
            stdout_handler = logging.StreamHandler(stream=sys.stdout)
            handlers = [file_handler, stdout_handler]
            logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG,
                                handlers=handlers)
            logging.debug('initializing')
        except BaseException as err:
            logging.error("Config: Error get_app_settings - {0}".format(err))
