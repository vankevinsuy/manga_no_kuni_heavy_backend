import pymongo as pymongo
import requests

import CommonVariables
from MongoDatabase.Database import Database


class MAL_manga_data(Database):
    def __init__(self):
        db = CommonVariables.Command_line['-d']
        self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'])
        self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]
        self.MAL_manga_data_collection = self.otaku_center_database["MAL_manga_data"]

    def getCollection(self):
        return self.MAL_manga_data_collection

    def getDocumentByID(self, id):
        return self.MAL_manga_data_collection.find_one({'mal_id' : id})

    def updateCollection(self):
        self.MAL_manga_data_collection.drop()
        for ficheManga in self.otaku_center_database["Fiche_manga_to_download"].find():
            myanimelist_id = ficheManga['myanimelist_id']
            MANGA_BASE_URL = "https://api.jikan.moe/v3/manga/{}"
            req = requests.get(MANGA_BASE_URL.format(myanimelist_id))

            if not self.MAL_manga_data_collection.count_documents({"mal_id" : myanimelist_id}) > 0:
                if req.status_code == 200:
                    self.MAL_manga_data_collection.insert(req.json())