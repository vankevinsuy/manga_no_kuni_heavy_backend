import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'local' : {
        "client" : "mongodb://{}:{}@192.168.1.22:27017/?authSource=Otaku_center",
        "database" : "Otaku_center"
    }
}

# valeur par default de la ligne de commande
Command_line = {'-d' : "local", # database, correspond à une des clefs de DATABASES
                '-f' : "none"   # fonction à lancer
                }

RETURN_STATEMENT = {
                    }