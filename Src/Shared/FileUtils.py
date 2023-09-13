import os
import json
import logging
from Src.Entites.Plant import Plant


class FileUtils:
    def __init__(self):
        pass

    def get_plants(self) -> list[Plant]:
        """
          Returns a list of the plants after creating each one to an object of type plant.
          :return: receive list of plants
          :rtype: list[Plant]
        """
        try:
            plants = [Plant]
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            plants_path = os.path.join(base_path, "Assets/Data/plants.json")
            if os.path.isfile(plants_path):
                with open(plants_path) as f:
                    ret = json.load(f)
                    plants = [Plant(item['name'], item['species'], item['age'], item['water_level'],
                                    item['water_requirement'], item['light_requirement'], item['height'])
                              for item in ret['Plants']]
            return plants
        except FileNotFoundError:
            logging.error(f"FileUtils: plants not found")
        except Exception as err:
            logging.error(f"FileUtils: Error get_plants - {err}")

    def get_read_me_file(self) -> str:
        """
        The function reads the readme file.
        :return: Returns the text that exists in the file
        :rtype: str
        """
        try:
            with open("README.md", "r", encoding="utf-8") as readme_file:
                readme_contents = readme_file.read()
                return readme_contents
        except FileNotFoundError:
            print("FileUtils : README.md file not found.")
        except Exception as e:
            print(f"FileUtils : An error occurred: {str(e)}")
