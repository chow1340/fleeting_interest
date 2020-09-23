from pymongo import MongoClient


class MongoConnectionConfig:
    def __init__(self):
        print("hello")

    @staticmethod
    def connect():
        return MongoClient("localhost:27017")
