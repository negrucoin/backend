from rest_framework import serializers


class MoneyCountSerializer(serializers.Serializer):
    money = serializers.IntegerField()
