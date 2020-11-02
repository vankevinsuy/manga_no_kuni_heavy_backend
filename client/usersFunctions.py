# ensemble des fonctions dédiées aux utilisateurs

from flask import request
import pymongo
import os
import CommonVariables
from MongoDatabase.Users import Users


class UserFunctions():
    def __init__(self, pseudo, password):
        self.pseudo = pseudo
        self.password = password
        self.connection_verified = False

        db = CommonVariables.Command_line['-d']

        try:
            self.my_client = pymongo.MongoClient("192.168.1.14:27017")
            con = self.my_client["Otaku_center"].authenticate(self.pseudo, self.password)

            if con:
                self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'].format(self.pseudo, self.password))
                self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]
                self.connection_verified = True
        except:
            CommonVariables.RETURN_STATEMENT["connected"] = -1
            CommonVariables.RETURN_STATEMENT["message"] = "connection failed verify pseudo and password"
            pass

        #self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'].format(self.pseudo, self.password))
        #self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]


    # obtenir tous les mangas selon la limite
    def getAllManga(self):
        if not self.connection_verified:
            return CommonVariables.RETURN_STATEMENT

        limit = int(request.args.get('limit'))

        manga_collection = self.otaku_center_database["Manga_we_have"]

        res = {'result' : []}

        for manga in manga_collection.find().sort("name", 1).limit(limit):
            manga['_id'] = str(manga['_id'])
            res['result'].append(manga)

        return res


    def testImage(self):
        res = ""

        for manga in os.listdir(CommonVariables.ROOT_DIR + '/LOCALdata'):
            try:
                for chapitre in os.listdir(CommonVariables.ROOT_DIR + '/LOCALdata/{}'.format(manga)):
                    for image in os.listdir(CommonVariables.ROOT_DIR + '/LOCALdata/{}/{}'.format(manga, chapitre)):
                        res = " http://192.168.1.14:1987/scans/{}/{}/{}".format(manga, chapitre, image)
                        return res
            except:
                pass