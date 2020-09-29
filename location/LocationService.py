from config.MongoConnectionConfig import MongoConnectionConfig
from bson import json_util, ObjectId

class LocationService(object):

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

    def updateLocation(self, location, currentId):
        self.users.update_one({'_id' : ObjectId(currentId)}, {'$set': {'location':location}}, upsert=False) 
        return "Location has been successfully updated"
         
     