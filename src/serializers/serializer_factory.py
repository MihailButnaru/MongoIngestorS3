# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from src.serializers.csv_serializer import CSVSerializer

class SerializerFactory:
    """
    Serializer Interface, customized behaviour
    based on different type object, different format
    """
    def get_serializer(self, format):
        """
        It evaluates the value of the format and decides
        the concrete implementation to create and return
            Args:
                format (str): type of the format
        """
        if format == 'csv':
            return CSVSerializer()
        else:
            raise ValueError(format)
            

factory = SerializerFactory()