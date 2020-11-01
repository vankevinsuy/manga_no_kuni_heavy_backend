import pymongo

import CommonVariables
from MongoDatabase.Database import Database
import hashlib


class Users(Database):
    def __init__(self):
        self.db = CommonVariables.Command_line['-d']
        self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[self.db]['client'])
        self.otaku_center_database = self.my_client[CommonVariables.DATABASES[self.db]["database"]]
        self.users_collection = self.otaku_center_database["Users"]

    def getCollection(self):
        super().getCollection()

    def getDocumentByID(self, id):
        super().getDocumentByID(id)

    def addNewUser(self, pseudo, password):
        # hasher le password pour la sécurité
        hashed_pseudo = hashlib.md5(pseudo.encode()).hexdigest()
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        # vérifier si le pseudo existe déjà en base
        user_exist_already = self.users_collection.find({'hashed_pseudo': hashed_pseudo}).count()
        if(user_exist_already >= 1):
            return False

        else:
            try :
                self.users_collection.insert({
                    'pseudo': pseudo,
                    'hashed_pseudo' : hashed_pseudo,
                    'password': hashed_password,
                    'list_manga_reading': [],
                    'status' : "client"
                })
                self.otaku_center_database.add_user(pseudo, password, roles=[{'role':'read','db':CommonVariables.DATABASES[self.db]["database"]}])
                return True

            except:
                print("user not added")
                return False

