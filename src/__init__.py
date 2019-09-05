# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from src.connectors.mongo_connector import init_mongodb_connection
from src.connectors.aws_connector import init_aws_connection
from src.core.mongo_manager import MongoManager
from src.core.aws_manager import AWSManager
from src.config import Config

_config = Config()
mongo_manager = MongoManager(init_mongodb_connection(_config))
aws_manager = AWSManager(init_aws_connection(_config),_config)