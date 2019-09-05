# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import csv

class CSVSerializer:
    """
    CSV Serializer formats the dict into a csv format file
    """
    def serialize(self, documents):
        """
        Serializer:
            Args:
                documents (list): list of data
        """
        return self._save_csv_file(documents)

    def _save_csv_file(self, data):
        """
        Saves the data into a csv file on the current directory
        """
        file_names = data.keys() # name of the files
        dict_data = data
        try:
            for file_name in file_names:
                with open(file_name+'.csv', 'w') as output_file:
                    for document_key in dict_data[file_name]:
                        writer = csv.DictWriter(output_file, fieldnames=document_key.keys())
                        writer.writeheader()
                    for data in dict_data[file_name]:
                        writer.writerow(data)
            return file_names
        except IOError as error:
            raise ValueError(error)