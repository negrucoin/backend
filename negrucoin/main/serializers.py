from rest_framework import serializers


class MoneyCountSerializer(serializers.Serializer):
    money = serializers.IntegerField()


class TopPlayerSerializer(serializers.Serializer):
    avatar_url = serializers.URLField()
    nickname = serializers.CharField(max_length=255)
    coins = serializers.IntegerField(min_value=0)


class TopPlayersSerializer(serializers.Serializer):
    top_players = TopPlayerSerializer(many=True)
