from django.conf import settings
settings.configure()

import django
django.setup()

from rest_framework import serializers as rf_serializers
from utils import write_csv, FakeJson
import marshmallow
import serpy


class SimpleRF(rf_serializers.Serializer):
    foo = rf_serializers.ReadOnlyField()


class SimpleM(marshmallow.Schema):
    foo = marshmallow.fields.Str()

    class Meta:
        json_module = FakeJson()


class SimpleS(serpy.Serializer):
    foo = serpy.Field()


if __name__ == '__main__':
    data = {'foo': 'bar'}
    write_csv(__file__, data, SimpleRF, SimpleM().dumps, SimpleS, 100)
