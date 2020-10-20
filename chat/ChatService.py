from config.MongoConnectionConfig import MongoConnectionConfig
from bson import json_util, ObjectId
from bson.json_util import dumps
from datetime import timedelta

class ChatService():

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ChatService.__instance == None:
            ChatService()
        return ChatService.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if ChatService.__instance != None:
         raise Exception("This class is a singleton!")
      else: 
         ChatService.__instance = self    
         self.mongoConnection = MongoConnectionConfig.getInstance()
         self.mongo = self.mongoConnection.connect()
         self.users = self.mongo.db.users
         self.chat = self.mongo.db.chat
         

    def getChat(self, chatId):
        chat = self.chat.find_one({'_id': ObjectId(chatId)})
        return chat

    def updateLastMessage(self, chatId, message):
        self.chat.find_one_and_update({'_id': ObjectId(chatId)}, \
             {'$set': {'lastMessageSent' : message}})

    def updateLastMessageDate(self, chatId, date):
        self.chat.find_one_and_update({'_id': ObjectId(chatId)}, \
             {'$set': {'lastMessageDate': date }}, upsert=True)

    def updateTotalMessages(self, chatId): 
        self.chat.find_one_and_update({'_id': ObjectId(chatId)}, \
             {'$inc': {'totalMessages':1}})

    def setIsRead(self, chat, userId, isRead):

        if chat['user1']['_id'] == userId:
            user = "user1"
        else:
            user = "user2"
        self.chat.find_one_and_update({'_id': chat['_id']}, \
            {'$set': {user + '.hasRead' : isRead}})

        return
