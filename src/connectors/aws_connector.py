# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
AWS connector, creates a connection to access aws services
"""
import boto3


def init_aws_connection(config):
    """
    Set up a connection to access AWS services
        Args:
            config [os.env] : list of arguments
        Returns:
            AWS client instance
    """
    return boto3.client(
        config.AWS_SERVICE,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        region_name=None
    )
