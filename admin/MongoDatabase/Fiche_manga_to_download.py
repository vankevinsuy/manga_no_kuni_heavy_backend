import pymongo as pymongo

import CommonVariables
from MongoDatabase.Database import Database


class Fiche_manga_to_download(Database):

    def __init__(self):
        db = CommonVariables.Command_line['-d']
        self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'])
        self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]
        self.fiche_manga_collection = self.otaku_center_database["Fiche_manga_to_download"]

    def getCollection(self):
        return self.fiche_manga_collection


    def getDocumentByID(self, id):
        return  self.fiche_manga_collection.find_one({'myanimelist_id': id})

