# ensemble des fonctions dédiées aux utilisateurs

from flask import request
import pymongo
import os
import CommonVariables
from MongoDatabase.Users import Users

db = CommonVariables.Command_line['-d']
my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'])
otaku_center_database = my_client[CommonVariables.DATABASES[db]["database"]]


def signup():
    pseudo = str(request.args.get('pseudo'))
    password = str(request.args.get('password'))

    action = Users().addNewUser(pseudo,password)

    if action :
        return "{} added".format(pseudo)
    else:
        return "User {} already in database choose another pseudo".format(pseudo)

# obtenir tous les mangas selon la limite
def getAllManga():
    limit = int(request.args.get('limit'))
    manga_collection = otaku_center_database["Manga_we_have"]

    res = {'result' : []}

    for manga in manga_collection.find().sort("name", 1).limit(limit):
        manga['_id'] = str(manga['_id'])
        res['result'].append(manga)

    return res


def testImage():
    res = ""

    for manga in os.listdir(CommonVariables.ROOT_DIR + '/LOCALdata'):
        try:
            for chapitre in os.listdir(CommonVariables.ROOT_DIR + '/LOCALdata/{}'.format(manga)):
                for image in os.listdir(CommonVariables.ROOT_DIR + '/LOCALdata/{}/{}'.format(manga, chapitre)):
                    res = " http://localhost:1987/scans/{}/{}/{}".format(manga, chapitre, image)
                    return res
        except:
            pass