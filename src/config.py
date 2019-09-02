# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import os

class Config:

    def MONGO_DB(self):
        """
        """
        return os.getenv('MONGO_DB', None)