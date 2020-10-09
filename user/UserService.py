from flask import Flask, render_template, url_for, request, session, redirect, Blueprint
from ServiceClass import ServiceClass
from bson import json_util, ObjectId
from bson.json_util import dumps
from config.MongoConnectionConfig import MongoConnectionConfig

class UserService(ServiceClass):

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if UserService.__instance == None:
            UserService()
        return UserService.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if UserService.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         UserService.__instance = self    
         self.mongoConnection = MongoConnectionConfig.getInstance()
         self.mongo = self.mongoConnection.connect()
         self.users = self.mongo.db.users
         
    def getCurrentUser(self):
        return session['phone_number']

    def getCurrentId(self):
        return session['_id']
    
    def getCurrentUserProfile(self):
        currentId = self.getCurrentId()
        user = self.users.find_one({'_id' : ObjectId(currentId)})
        return user

