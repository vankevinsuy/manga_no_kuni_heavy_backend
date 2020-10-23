import pymongo

import CommonVariables
from MongoDatabase.Database import Database
import hashlib


class Users(Database):
    def __init__(self, user, password):
        db = CommonVariables.Command_line['-d']
        self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'].format(user, password))
        self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]
        self.users_collection = self.otaku_center_database["Users"]

    def __init__(self):
        db = CommonVariables.Command_line['-d']
        self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'].format("root", "password"))
        self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]
        self.users_collection = self.otaku_center_database["Users"]

    def getCollection(self):
        super().getCollection()

    def getDocumentByID(self, id):
        super().getDocumentByID(id)
