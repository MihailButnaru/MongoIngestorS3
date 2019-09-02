# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Mongo database connector, connects to the mongo database based on the configuration
"""
from pymongo import MongoClient


def init_mongodb_connection(config):
    """
    Set up a connection to the MongoDB server
        Args:
            config [os.env] : list of arguments
        Returns:
            MongoClient instance
    """
    try:
        if config.MONGODB_USERNAME and config.MONGODB_PASSWORD:
            uri = 'mongodb://{}:{}@{}:{}/{}'.format(
                config.MONGODB_USERNAME,
                config.MONGODB_PASSWORD,
                config.MONGODB_HOST,
                config.MONGODB_PORT,
                config.MONGODB_NAME
            )
        else:
            uri = 'mongodb://{}:{}/{}'.format(
                config.MONGODB_HOST,
                config.MONGODB_PORT,
                config.MONGODB_NAME
            )
        connect = MongoClient(uri)
        return connect[config.MONGODB_NAME]
    except Exception:
        raise Exception('Could not connect to mongo database {} at {}:{}'.format(
                        config.MONGODB_NAME,
                        config.MONGODB_HOST,
                        config.MONGODB_PORT))
