from rest_framework import serializers

from watch_app.models import WatchList, StreamPlatform, Reviews


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'

    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='watch_app'
    # )

    # def get_len_name(self, object):
    #     return len(object.name)
    #
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description should not be same")
    #     else:
    #         return data
    #
    # def name_validate(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")

#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     rating = serializers.IntegerField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.rating = validated_data.get('rating', instance.rating)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
