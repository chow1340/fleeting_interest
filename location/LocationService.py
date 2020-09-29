from config.MongoConnectionConfig import MongoConnectionConfig
from ServiceClass import ServiceClass
from bson import json_util, ObjectId
from bson.json_util import dumps

class LocationService(ServiceClass):

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if LocationService.__instance == None:
            LocationService()
        return LocationService.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if LocationService.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         LocationService.__instance = self    

    def updateLocation(self, location, currentId):
        user = dumps(self.users.find_one_and_update({'_id' : ObjectId(currentId)}, {'$set': {'location':location}}, upsert=False, projection={'password': False})) 
        return user
         
    def updateGeocode(self, geocode, currentId):
        user = dumps(self.users.find_one_and_update({'_id' : ObjectId(currentId)}, {'$set': {'geocode':geocode}}, upsert=False, projection={'password': False})) 
        return user