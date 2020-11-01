# fonction de téléchargement pour le site : https://w11.mangafreak.net/
import io
import zipfile
import requests
from MongoDatabase.Error_log import Error_log
import datetime
from Tools import MangaFreakTestUrl
import CommonVariables

class MangaFreak():
    def DownloadScanFromUrl(self,url, directory_to_save):
        if MangaFreakTestUrl(url):
            try:
                r = requests.get(url)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(directory_to_save)
                CommonVariables.RETURN_STATEMENT['scan_downloaded'].append(url)

            except Exception as err:
                #ajouter un log de probleme dans la base de données
                Error_log().addError(
                    {
                        'date' : str(datetime.datetime.now()),
                        'function' : "MangafreakDownloadScanFromUrl(url, directory_to_save)",
                        'url' : url,
                        'directory_to_save' : directory_to_save,
                        'error' : err.args
                    }
                )
                print(err)
                CommonVariables.RETURN_STATEMENT['error_scan_downloaded'].append(url)
