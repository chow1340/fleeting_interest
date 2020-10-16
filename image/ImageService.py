from config.MongoConnectionConfig import MongoConnectionConfig
from settings import S3_BUCKETNAME
from user.UserService import UserService
from bson.json_util import dumps
from bson import json_util, ObjectId
import boto3


class ImageService():
    __instance = None

    userService = UserService.getInstance()

    @staticmethod
    def getInstance():
        """ Static access method. """
        if ImageService.__instance == None:
            ImageService()
        return ImageService.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if ImageService.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         ImageService.__instance = self    
         self.mongoConnection = MongoConnectionConfig.getInstance()
         self.mongo = self.mongoConnection.connect()
         self.users = self.mongo.db.users
         self.s3 = boto3.resource('s3')

    def uploadImageToS3(self, file):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(S3_BUCKETNAME)
        bucket.Object(file.filename).put(Body=file.read(), ACL='public-read')

        return file.filename

    def deleteImageFromS3(self, fileKey):
        return self.s3.Object(S3_BUCKETNAME, fileKey).delete()

    def getPictureArraySize(self, currentId):
        user = self.users.find_one({'_id' : ObjectId(currentId)})
        if "picture" in user:
            return len(user['picture'])
        else: 
            return 0



    def pushImageToUser(self, currentId, picture):
        pictureArraySize = self.getPictureArraySize(currentId)
        # TODO CHANGE THIS LIMIT IF NEEDED
        if pictureArraySize < 7:
            self.users.find_one_and_update({'_id' : ObjectId(currentId)}, \
                {'$push': {'picture': picture}}, upsert=True) 
        
    def setImageToIndex(self, currentId, index, picture):
        pictureArraySize = self.getPictureArraySize(currentId)

        if pictureArraySize == 0 or index > pictureArraySize:
            self.users.find_one_and_update({'_id' : ObjectId(currentId)}, \
                {'$push': {'picture': picture}}, upsert=True) 
        else:
            self.users.find_one_and_update({'_id' : ObjectId(currentId)}, \
                {'$set' : {'picture.'+ str(index) : picture}}, upsert=True)

    def deleteImageFromUserByPicture(self, currentId, picture):
        self.users.find_one_and_update({'_id': ObjectId(currentId)}, \
            {'$pull': {'picture' : picture}})

        
