from flask import Flask, session, Blueprint
from user.UserService import UserService
from chat.ChatService import ChatService
from bson import json_util, ObjectId
from config.MongoConnectionConfig import MongoConnectionConfig

class MatchService():


    __instance = None
    @staticmethod
    def getInstance():
        """ Static access method. """
        if MatchService.__instance == None:
            MatchService()
        return MatchService.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if MatchService.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         MatchService.__instance = self    
         self.mongoConnection = MongoConnectionConfig.getInstance()
         self.mongo = self.mongoConnection.connect()
         self.users = self.mongo.db.users
         self.chatService = ChatService.getInstance()

    def getMatchesByList(self, matchList):
        result = []

        for match in matchList:
            id= match['_id']
            user = self.users.find_one({'_id' : ObjectId(id)}, projection={'password': False})
            
            #Get chat
            chat = self.chatService.getChat(match["chatId"])
            result.append({"user":user, "chatId" : match["chatId"], "chat" : chat})

        return result



