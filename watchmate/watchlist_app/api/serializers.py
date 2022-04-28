from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from watchlist_app.models import Movie
from watchlist_app.models import StreamPlatform, WatchList,Review

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Movie.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.active=validated_data.get('active',instance.active)
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

class WatchlistSerializer(serializers.ModelSerializer):
    review=ReviewSerializer(many=True,read_only=True)

    class Meta:
        model=WatchList
        fields="__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist=WatchlistSerializer(many=True,read_only=True)
    watchlist=serializers.StringRelatedField(many=True)
    class Meta:
        model=StreamPlatform
        fields="__all__"

