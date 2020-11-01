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

        db = CommonVariables.Command_line['-d']
        self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'])
        self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]


    # obtenir tous les mangas selon la limite
    def getAllManga(self):
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