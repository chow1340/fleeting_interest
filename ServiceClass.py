from config.MongoConnectionConfig import MongoConnectionConfig
import boto3


class ServiceClass():
    def __init__(self):
        self.mongoConnection = MongoConnectionConfig.getInstance()
        self.mongo = self.mongoConnection.connect()
        self.users = self.mongo.db.users
        self.s3 = boto3.resource('s3')
