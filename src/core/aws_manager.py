# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
AWS manager will handle all the operations related to the s3 service
"""

class AWSManager:
    """
    AWS Manager handles the S3 operations 
    """
    def __init__(self, connection, config):
        self._connection = connection
        self._config = config

    def bucket_manager(self, files, format):
        """
        Helper that checks and assigns a format to each file
        to be saved in a bucket
        """
        try:
            for file_name in files:
                self._send_file_bucket(file_name+'.'+format)
        except ValueError as error:
            raise ValueError(error)


    def _send_file_bucket(self, filename):
        """
        Sends a file to S3 to the correct bucket
        that is specified in the configuration file
        """
        self._connection.upload_file(
            filename, 
            self._config.AWS_BUCKET_NAME,
            filename
        )