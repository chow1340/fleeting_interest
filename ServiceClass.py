from config.MongoConnectionConfig import MongoConnectionConfig


class ServiceClass():
    def __init__(self):
        self.mongoConnection = MongoConnectionConfig.getInstance()
        self.mongo = self.mongoConnection.connect()
        self.users = self.mongo.db.users