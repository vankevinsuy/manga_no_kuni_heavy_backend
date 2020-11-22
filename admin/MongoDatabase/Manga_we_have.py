import errno
import os

import pymongo

import CommonVariables
from MongoDatabase.Database import Database
from MongoDatabase.Fiche_manga_to_download import Fiche_manga_to_download
from MongoDatabase.MAL_manga_data import MAL_manga_data


class Manga_we_have(Database):
    def __init__(self):
        db = CommonVariables.Command_line['-d']
        self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'])
        self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]
        self.Manga_we_have_collection = self.otaku_center_database["Manga_we_have"]

    def getCollection(self):
        return self.Manga_we_have_collection

    def getDocumentByID(self, id):
        return self.Manga_we_have_collection.find_one({'myanimelist_id' : id})

    def updateCollection(self):
        self.Manga_we_have_collection.drop()
        FichemangaCollection = Fiche_manga_to_download().getCollection()
        toInsert = []

        for manga in os.listdir(CommonVariables.ROOT_DIR + "/LOCALdata"):
            try:
                chapterAsPDF = ""
                listChapterPage = []
                Manga_data = FichemangaCollection.find_one({"myanimelist_id": int(manga.split('_')[1])})
                last_chapter = 1

                for chapter in os.listdir(CommonVariables.ROOT_DIR + "/LOCALdata/{}".format(manga)):
                    listPage = []

                    print("{}  chapter : {} files = {}".format(manga, chapter, os.listdir(
                        CommonVariables.ROOT_DIR + "/LOCALdata/{}/{}".format(manga, chapter))))
                    if int(chapter) > last_chapter:
                        last_chapter = int(chapter)

                    for file in os.listdir(CommonVariables.ROOT_DIR + "/LOCALdata/{}/{}".format(manga, chapter)):
                        if file.split(".")[1] == "jpg" or \
                                file.split(".")[1] == "jpeg" or \
                                file.split(".")[1] == "png":
                            listPage.append(file)
                        if file.split(".")[1] == "pdf":
                            chapterAsPDF = file

                    listChapterPage.append({chapter: listPage, "{}_as_pdf".format(chapter): chapterAsPDF})

                toInsert.append({
                    "name": Manga_data['manga_name'],
                    "myanimelist_id": Manga_data['myanimelist_id'],
                    "poster_image": MAL_manga_data().getDocumentByID(int(Manga_data['myanimelist_id']))[
                        'image_url'],
                    "last_chapter": last_chapter,
                    "chapitres": listChapterPage,
                })
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise

        for dic in toInsert:
            self.Manga_we_have_collection.insert(
                {
                    "name": dic['name'],
                    "myanimelist_id": dic['myanimelist_id'],
                    "poster_image": dic['poster_image'],
                    "last_chapter": dic['last_chapter'],
                })

            for chapt in dic["chapitres"]:
                self.Manga_we_have_collection.update({'myanimelist_id': dic['myanimelist_id']},
                                                     {"$push": {"chapitres": chapt}})


