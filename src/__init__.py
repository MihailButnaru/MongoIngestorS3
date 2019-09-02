# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from src.connectors.mongo_connector import init_mongodb_connection
from src.core.mongo_manager import MongoManager
from src.config import Config

_config = Config()
client = init_mongodb_connection(_config)
mongo = MongoManager(client)