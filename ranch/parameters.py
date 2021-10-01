import os
from .logger import RanchLogger

def get_base_dir(ranch_base_dir=os.getcwd()):
    d = ranch_base_dir
    for i in range(3):
        if "ranch" in os.listdir(d):
            RanchLogger.info("Lasso base directory set as: {}".format(d))
            return d
        d = os.path.dirname(d)

    msg = "Cannot find ranch base directory from {}, please input using keyword in parameters: `ranch_base_dir =` ".format(
        ranch_base_dir
    )
    RanchLogger.error(msg)
    raise (ValueError(msg))

class Parameters:
    """A class representing all the parameters

    """

    def __init__(self, **kwargs):
        """
        Time period and category  splitting info
        """
        if "ranch_base_dir" in kwargs:
            self.base_dir = get_base_dir(ranch_base_dir=kwargs.get("ranch_base_dir"))
        else:
            self.base_dir = get_base_dir()

        if "settings_location" in kwargs:
            self.settings_location = kwargs.get("settings_location")
        else:
            self.settings_location = os.path.join(self.base_dir, "settings")

        self.highway_to_roadway_crosswalk_file = os.path.join(self.settings_location, "highway_to_roadway.csv")

        self.network_type_file = os.path.join(self.settings_location, "network_type_indicator.csv")

        self.county_node_range = {
            "San Francisco" : {"start" : 1000000, "end" : 1500000},
            "San Mateo" : {"start" : 1500000, "end" : 2000000},
            "Santa Clara" : {"start" : 2000000, "end" : 2500000},
            "Alameda" : {"start" : 2500000, "end" : 3000000},
            "Contra Costa" : {"start" : 3000000, "end" : 3500000},
            "Solano" : {"start" : 3500000, "end" : 4000000},
            "Napa" : {"start" : 4000000, "end" : 4500000},
            "Sonoma" : {"start" : 4500000, "end" : 5000000},
            "Marin" : {"start" : 5000000, "end" : 5250000},
            "San Joaquin" : {"start" : 5250000, "end" : 5500000},
        }

        self.county_link_range = {
            "San Francisco" : {"start" : 1, "end" : 1000000},
            "San Mateo" : {"start" : 1000000, "end" : 2000000},
            "Santa Clara" : {"start" : 2000000, "end" : 3000000},
            "Alameda" : {"start" : 3000000, "end" : 4000000},
            "Contra Costa" : {"start" : 4000000, "end" : 5000000},
            "Solano" : {"start" : 5000000, "end" : 6000000},
            "Napa" : {"start" : 6000000, "end" : 7000000},
            "Sonoma" : {"start" : 7000000, "end" : 8000000},
            "Marin" : {"start" : 8000000, "end" : 8500000},
            "San Joaquin" : {"start" : 8500000, "end" : 9000000},
        }

        self.__dict__.update(kwargs)