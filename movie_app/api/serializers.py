from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    rating = serializers.IntegerField()
    description = serializers.CharField()
    active = serializers.BooleanField()
