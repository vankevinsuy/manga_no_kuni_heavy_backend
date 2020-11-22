# ensemble des fonctions dédiées aux admins
import errno
import os

from MongoDatabase.Fiche_manga_to_download import Fiche_manga_to_download
from MongoDatabase.MAL_manga_data import MAL_manga_data
from MongoDatabase.Manga_we_have import Manga_we_have
from MongoDatabase.Users import Users

from WebsiteDownloader.Mangafreak import MangaFreak
import CommonVariables
from Tools import imagesToPDF, MangaFreakTestUrl


def download_all_scan():
    CommonVariables.RETURN_STATEMENT['function launched'] = "download_all_scan"
    fiche_manga_collection = Fiche_manga_to_download().getCollection()


    for fiche_manga in fiche_manga_collection.find():
        # verifier si un dossier existe pour ce manga
        try:
            os.makedirs(CommonVariables.ROOT_DIR + "/LOCALdata/{}_{}".format(
                fiche_manga['manga_name'],
                fiche_manga['myanimelist_id']))
        except OSError as e:
            if e.errno != errno.EEXIST:
                CommonVariables.RETURN_STATEMENT['error' : str(e.args)]
                raise

        # télécharger chapitre par chapitre
        for num_chapitre in range(fiche_manga['last_chapter_download'], fiche_manga['last_chapter'] + 1):
            # verifier si un dossier existe pour ce chapitre
            try:
                os.makedirs(
                    CommonVariables.ROOT_DIR + "/LOCALdata/{}_{}/{}".format(
                        fiche_manga['manga_name'],
                        fiche_manga['myanimelist_id'],
                        num_chapitre)
                )
            except OSError as e:
                if e.errno != errno.EEXIST:
                    CommonVariables.RETURN_STATEMENT['error': str(e.args)]
                    raise


            working_directory = CommonVariables.ROOT_DIR + "/LOCALdata/{}_{}/{}".format(fiche_manga['manga_name'], fiche_manga['myanimelist_id'],num_chapitre)

            for key in fiche_manga['link_dict']:
                print(fiche_manga['link_dict'][key].format(num_chapitre))

                # selon le site on choisi la fonction de téléchargement
                if key == "mangaFreak":
                    MangaFreak().DownloadScanFromUrl(fiche_manga['link_dict'][key].format(num_chapitre),working_directory)

                # créer un pdf à partir des images téléchargées
                imagesToPDF(working_directory,fiche_manga['pattern_dict'][key].format(str(num_chapitre), '{}', '{}').split('{}')[0])

                # mettre à jour la vlaeur de "last_chapter_download" dans la base de données
                fiche_manga_collection.update_one({"myanimelist_id": fiche_manga['myanimelist_id']},
                                                  {"$set": {"last_chapter_download": num_chapitre}})
                pass

def MAL_manga_data_update():
    MAL_manga_data().updateCollection()

def Manga_we_have_update():
    Manga_we_have().updateCollection()

def updateScan():
    fiche_manga_collection = Fiche_manga_to_download().getCollection()

    for fiche_manga in fiche_manga_collection.find():
        last_chapter = fiche_manga['last_chapter']

        #tester le prochain chapitre pour toutes les urls
        for key in fiche_manga['link_dict']:
            index = 1
            url = fiche_manga['link_dict'][key].format(last_chapter + index)

            while MangaFreakTestUrl(url):
                print(url)

                # créer un dossier pour le nouveau chapitre
                try:
                    os.makedirs(
                        CommonVariables.ROOT_DIR + "/LOCALdata/{}_{}/{}".format(fiche_manga['manga_name'],
                                                                                fiche_manga['myanimelist_id'],
                                                                                last_chapter + index))
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise

                # télécharger les scans
                LocalData_manga_directory = CommonVariables.ROOT_DIR + "/LOCALdata/{}_{}/{}".format(fiche_manga['manga_name'], fiche_manga['myanimelist_id'], last_chapter + index)
                MangaFreak().DownloadScanFromUrl(url, LocalData_manga_directory)
                imagesToPDF(LocalData_manga_directory, fiche_manga['pattern_dict'][key].format(str(last_chapter + index), '{}', '{}').split('{}')[0])

                # mettre à jour la base de données
                fiche_manga_collection.update({'myanimelist_id' : fiche_manga['myanimelist_id']}, {"$set": { "last_chapter": last_chapter + index }})
                fiche_manga_collection.update({'myanimelist_id' : fiche_manga['myanimelist_id']}, {"$set": { "last_chapter_download": last_chapter + index }})

                index = index + 1
                url = fiche_manga['link_dict'][key].format(last_chapter + index)

    MAL_manga_data_update()
    Manga_we_have_update()

def signup(pseudo, password):
    Users().addNewUser(pseudo, password)

