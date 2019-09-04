# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from src.serializers.serializer_factory import factory

class Serializer:
    """
    Generic implementation of the format serializer
    """
    def serializer(self, serializable, service):
        serializer = factory.get_serializer(service)
        return serializer.serialize(serializable)

serialize = Serializer()