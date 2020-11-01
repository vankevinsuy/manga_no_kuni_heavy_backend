import pymongo as pymongo

import CommonVariables


class Error_log :
    def __init__(self, user, password):
        db = CommonVariables.Command_line['-d']
        self.my_client = pymongo.MongoClient(CommonVariables.DATABASES[db]['client'].format(user, password))
        self.otaku_center_database = self.my_client[CommonVariables.DATABASES[db]["database"]]
        self.error_log_collection = self.otaku_center_database["Error_log"]


    def addError(self, dic_error):
        self.error_log_collection.insert(dic_error)
