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


    ######## ============[  MONGO DATABASE CONFIGURATIONS  ]============

    @property
    def AWS_SERVICE(self):
        """
        Specify the name of the aws service
        """
        return os.getenv('AWS_SERVICE', None)

    @property
    def AWS_ACCESS_KEY_ID(self):
        """
        Specify the aws access key ID
        """
        return os.getenv('AWS_ACCESS_KEY_ID', None)

    @property
    def AWS_SECRET_ACCESS_KEY(self):
        """
        Specify the aws secret access key
        """
        return os.getenv('AWS_SECRET_ACCESS_KEY', None)

    @property
    def AWS_REGION_NAME(self):
        """
        Specify the aws region name
        """
        return os.getenv('AWS_REGION_NAME', None)
