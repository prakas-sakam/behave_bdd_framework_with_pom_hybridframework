from configparser import ConfigParser
def config_reader(category,key):
    config = ConfigParser()
    config.read(r"configurations/config.ini")
    return config.get(category, key)
