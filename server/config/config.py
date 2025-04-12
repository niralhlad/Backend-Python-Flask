import configparser

class Config:
    def __init__(self):
        print("init config.py")
        config = configparser.ConfigParser()
        config.read("./configfile.ini")
        self.__CONFIG_DETAILS = config["config_details"]

    def getDBConfig(self):
        dbConfig = {}
        dbConfig['dbHost'] = self.__CONFIG_DETAILS['db_host']
        dbConfig['dbUser'] = self.__CONFIG_DETAILS['db_user']
        dbConfig['dbPassword'] = self.__CONFIG_DETAILS['db_password']
        dbConfig['dbName'] = self.__CONFIG_DETAILS['db_name']
        dbConfig['dbPort'] = self.__CONFIG_DETAILS['db_port']

        return dbConfig

    def getHostConfig(self):
        hostConfig = {}
        hostConfig['port'] = self.__CONFIG_DETAILS['host_port']
        hostConfig['host'] = self.__CONFIG_DETAILS['host_address']
        return hostConfig
    
    def getDebugMode(self):
        return self.__CONFIG_DETAILS['debug_mode']