from config.MongoConnectionConfig import MongoConnectionConfig
from bson import json_util, ObjectId
from bson.json_util import dumps
from pymongo import GEO2D

class LocationService():

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
         self.mongoConnection = MongoConnectionConfig.getInstance()
         self.mongo = self.mongoConnection.connect()
         self.users = self.mongo.db.users
        #  self.users.create_index([("coordinates",GEO2D)])
    
         
    def updateLocation(self, location, currentId):
        coordinates = [location['coords']['longitude'], location['coords']['latitude']]
        user = dumps(self.users.find_one_and_update({'_id' : ObjectId(currentId)}, {'$set': {'location':location, 'coordinates':coordinates}}, upsert=False, projection={'password': False})) 
        return user
         
    def updateGeocode(self, geocode, currentId):
        user = dumps(self.users.find_one_and_update({'_id' : ObjectId(currentId)}, {'$set': {'geocode':geocode}}, upsert=False, projection={'password': False})) 
        return user
        
    def getNearbyUsers(self, coordinates, maxDistance):
        users = dumps(self.users.find({"coordinates": {"$near" : 
            {"$geometry" : {
                "type": "Point", "coordinates": coordinates
                }, 
            "$maxDistance" : maxDistance #In meters ?
            }}}))
        return users