from pymongo import MongoClient


class MongoConnectionConfig:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if MongoConnectionConfig.__instance == None:
            MongoConnectionConfig()
        return MongoConnectionConfig.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if MongoConnectionConfig.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         print("hello")
         MongoConnectionConfig.__instance = self    

    @staticmethod
    def connect():
        return MongoClient("localhost:27017")
        
