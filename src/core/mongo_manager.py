# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Mongo manager will handle all the operations related to the mongo database
"""

class MongoManager():
    """
    Mongo Manager handles the collections and documents from a collection
    in a storage.
    """
    def __init__(self, connection):
        self._connection = connection

    def get_data_collection(self):
        """
        Data is collected and stored in a list from
        mongo database, each collection is stored in a list
        then in a dict.
            Returns:
                dict with all the data from the collections
        """
        storage_documents = dict()
        documents = []

        for collection in self._get_collections():
            for document in collection.find({}, {'_id': 0}):
                documents.append(document)
            storage_documents[collection.name] = documents
            documents = []
        return storage_documents

    def _get_collections(self):
        """
        Based on the configuration, table name a
        list of collections from mongo database is returned.
        """
        collections = self._connection.list_collection_names()
        return [self._connection[collection] for collection in collections]
