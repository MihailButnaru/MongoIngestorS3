# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Mongo manager will handle all the operations related to the mongo database
"""
class MongoManager():
    """
    """
    def __init__(self, connection):
        self._connection = connection


    def get_collections(self):
        """
        List available collections in the mongo database
        """
        return self._connection.collection_names()