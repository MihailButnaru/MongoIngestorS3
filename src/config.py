# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import os

class Config:

    ######## ============[  MONGO DATABASE CONFIGURATIONS  ]============

    @property
    def MONGODB_NAME(self):
        """
        Specify the name of the mongo database
        """
        return os.getenv('MONGODB_NAME', 'gymManagement')
    
    @property
    def MONGODB_HOST(self):
        """
        Specify the host of the mongo database
            [localhost] default
        """
        return os.getenv('MONGODB_HOST', 'localhost')

    @property
    def MONGODB_PORT(self):
        """
        Specify the port of the mongo database 
            [27017] default
        """
        return os.getenv('MONGODB_PORT', 27017)

    @property
    def MONGODB_USERNAME(self):
        """
        Specify the username of the mongo database
        """
        return os.getenv('MONGODB_USERNAME', None)

    @property
    def MONGODB_PASSWORD(self):
        """
        Specify the password of the mongo database
        """
        return os.getenv('MONGODB_PASSWORD', None)