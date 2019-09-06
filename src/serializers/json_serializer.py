# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import json

class JSONSerializer:
    """
    JSON Serializer formats the data into a json file
    """
    def serialize(self, documents):
        """
        Serializer:
            Args:
                documents (list): list of data
        """
        self._format_json_documents(documents)

    def _format_json_documents(self, data):
        """
        Checks each document and it clean the unwanted symbols
        """
        file_names = data.keys()
        try:
            for file_name in file_names:
                self._save_json_file(
                    file_name, 
                    data[file_name])
        except IOError as error:
            raise ValueError(error)



    def _save_json_file(self, file_name, data):
        """
        Saves the data into a json file on the current directory
        """
        with open(file_name+'.json', 'w') as json_file:
            json.dump({file_name: data}, json_file)