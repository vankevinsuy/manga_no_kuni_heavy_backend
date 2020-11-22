# classe abstraite qui définie la structure de tout les table de la base de données

from abc import ABC,abstractmethod


class Database(ABC):

    def getCollection(self):
        pass

    def getDocumentByID(self, id):
        pass

    def updateCollection(self):
        pass